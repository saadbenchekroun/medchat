import streamlit as st

# Streamlit App
st.title("Contact Support")

st.write("We're here to help! Please fill out the form below, and our team will get back to you as soon as possible.")

# User Inputs
with st.form("contact_form"):
    name = st.text_input("Name", placeholder="Enter your full name")
    email = st.text_input("Email", placeholder="Enter your email address")
    message = st.text_area("Message", placeholder="Describe your issue or question here...")
    submit_button = st.form_submit_button("Submit")

# Form Handling
if submit_button:
    if name and email and message:
        st.success(f"Thank you, {name}! Your message has been sent. We'll respond to {email} shortly.")
        # Add code here to send the message to your email or save to a database
        # Example: save_to_database(name, email, message) or send_email(name, email, message)
    else:
        st.error("Please fill out all fields before submitting.")

# Additional Information
st.write("Alternatively, you can reach us via email at **medchat@gmail.com** or call us at **+123 456 789**.")
