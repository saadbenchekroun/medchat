import streamlit as st

# Page Title
st.title("Your Details")
st.subheader("Help us make the prediction better")

col1, col2 = st.columns(2)

with col1:
    with st.form("user_details_form"):
        st.write("### Basic Information")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        gender = st.radio("Gender", options=["Male", "Female", "Other"])

        st.write("### Body Measurements")
        height = st.number_input("Height (cm)", min_value=0.0, step=0.1)
        weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1)
        submitted = st.form_submit_button("Submit")

with col2:
    with st.form("user_life_form"):
        st.write("### Lifestyle Information")
        activity_level = st.selectbox(
            "Activity Level", 
            options=["Sedentary", "Lightly Active", "Moderately Active", "Very Active"]
        )
        smoking_status = st.radio("Do you smoke?", options=["Yes", "No"])
        alcohol_consumption = st.radio("Do you consume alcohol?", options=["Yes", "No"])

        st.write("### Health Details")
        pre_existing_conditions = st.text_area(
            "Any pre-existing conditions or medical history?", 
            placeholder="E.g., diabetes, hypertension, allergies"
        )
        medications = st.text_area(
            "Are you taking any medications?", 
            placeholder="E.g., painkillers, insulin"
        )

        # Submit Button
        submitted = st.form_submit_button("Submit")

# Process Form Submission
if submitted:
    st.success("Thank you for sharing your details!")
    st.write("### Summary of Your Details")
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Height:** {height} cm")
    st.write(f"**Weight:** {weight} kg")
    st.write(f"**Activity Level:** {activity_level}")
    st.write(f"**Smoking Status:** {smoking_status}")
    st.write(f"**Alcohol Consumption:** {alcohol_consumption}")
    st.write(f"**Pre-existing Conditions:** {pre_existing_conditions if pre_existing_conditions else 'None'}")
    st.write(f"**Medications:** {medications if medications else 'None'}")
