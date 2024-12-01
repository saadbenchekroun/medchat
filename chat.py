import streamlit as st
import os
from PIL import Image
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the Llama-3.2-11B-Vision-Instruct model
model_name = "unsloth/Llama-3.2-11B-Vision-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to("cuda")

st.title("Medchat")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display options for uploading an image or using the camera
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

with col2:
    picture = st.camera_input("Take a picture", key="camera", help="Capture image", disabled=False)

def resize_image(image, max_width=100, max_height=100):
    image.thumbnail((max_width, max_height))
    return image

if uploaded_file or picture:
    image = Image.open(uploaded_file or picture)
    st.image(image, caption="Uploaded or Captured Image")

    # Prepare the image for the model
    instruction = """You are an expert radiographer.
    Carefully examine the provided medical image.
    Describe your observations accurately and comprehensively, including any abnormalities or significant features.
    Based on your expertise, suggest the next steps or potential solutions, if applicable.
    Ensure your response is clear, concise, and professional."""

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image"},
                {"type": "text", "text": instruction}
            ]
        }
    ]

    input_text = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
    inputs = tokenizer(
        image,
        input_text,
        return_tensors="pt",
        add_special_tokens=False
    ).to("cuda")

    # Chat input section
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("What is up?")
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            text_streamer = TextStreamer(tokenizer, skip_prompt=True)
            response = model.generate(
                **inputs,
                streamer=text_streamer,
                max_new_tokens=125,
                use_cache=True,
                temperature=1.5,
                min_p=0.1
            )
            for token in response:
                full_response += token
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
