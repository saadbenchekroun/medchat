import streamlit as st

#streamlit run app.py

st.set_page_config(layout="wide")

# Set up the sidebar layout
st.sidebar.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

# Display the image with a specific width
st.sidebar.image(
    "./image.png",
    width=150
)

# Close the centered div
st.sidebar.markdown("</div>", unsafe_allow_html=True)

# Add a spacer to push the image to the bottom
st.sidebar.markdown("<div style='height: 100%;'></div>", unsafe_allow_html=True)


# Define your gradient background a2c5ea
gradient_style = """
<style>
.stApp {
    background-image: linear-gradient(to right, #424d7e, #343b58);
    color: white; /* Optional: Change text color */
}
</style>
"""

# Inject the CSS
st.markdown(gradient_style, unsafe_allow_html=True)

pages = {
    "Your account": [
        st.Page("chat.py", title="Medchat"),
        st.Page("data.py", title="Your health data"),
        st.Page("appointment.py", title="Book appointment"),
    ],
    "Resources": [
        st.Page("learn.py", title="Educational Resources"),
        st.Page("support.py", title="Contact Support"),
    ],
}

pg = st.navigation(pages)
pg.run()