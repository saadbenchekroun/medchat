import streamlit as st
import os
from mistralai import Mistral
from base64 import b64encode
from PIL import Image
import io

# Initialize Mistral client
api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"
client = Mistral(api_key=api_key)

st.title("Medchat")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display options for uploading an image or using the camera
col1, col2 = st.columns(2)

# Column for file upload
with col1:
    uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

# Column for camera input
with col2:
    picture = st.camera_input("Take a picture", key="camera", help="Capture image", disabled=False)

def resize_image(image, max_width=100, max_height=100):
    # Resize image while maintaining aspect ratio
    image.thumbnail((max_width, max_height))
    return image

if uploaded_file:
    # Read and process the uploaded image
    image = Image.open(uploaded_file)
    resized_image = resize_image(image)
    
    # Display resized image
    st.image(resized_image, caption="Uploaded Image")
    
    # Optional: Encode if needed for further processing
    buffered = io.BytesIO()
    resized_image.save(buffered, format="PNG")
    encoded_image = b64encode(buffered.getvalue()).decode("utf-8")

elif picture:
    # Process camera input image
    image = Image.open(picture)
    resized_image = resize_image(image)
    
    # Display resized image
    st.image(resized_image, caption="Captured Image", use_column_width=True)
    
    # Optional: Encode if needed for further processing
    buffered = io.BytesIO()
    resized_image.save(buffered, format="PNG")
    encoded_image = b64encode(buffered.getvalue()).decode("utf-8")


# Chat input section
if uploaded_file or picture:  # Enable chat input only after an image is uploaded or captured
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    prompt = st.chat_input("What is up?")
    if prompt:
        # Display user message in chat
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display assistant's response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            # Mistral API streaming response
            stream_response = client.chat.stream(
                model=model,
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                metadata={"image": encoded_image}  # Include image data in metadata
            )
            for chunk in stream_response:
                content_chunk = chunk.data.choices[0].delta.content
                full_response += content_chunk
                message_placeholder.markdown(full_response + "▌")  # Add typing effect
            message_placeholder.markdown(full_response)  # Final response
        # Add assistant's response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})