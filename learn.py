import streamlit as st

# Educational blogs for each modality
def get_blog(modality):
    blogs = {
        "Radiographie": (
            "Radiography, commonly known as X-ray imaging, is a painless and quick procedure. "
            "It is one of the most commonly used diagnostic tools in medicine, allowing doctors to see inside the body without any invasive procedure. "
            "X-rays are safe, and the level of radiation exposure is very low. Modern technology ensures that the risks are minimal, while the benefits of early and accurate diagnosis are immense."
        ),
        "Scanner": (
            "A CT scan, also known as a CAT scan, uses advanced X-ray technology to take detailed cross-sectional images of your body. "
            "It is a powerful tool that helps doctors diagnose conditions with great precision. "
            "The process is fast, painless, and non-invasive. While some may worry about radiation, the levels used are carefully controlled to ensure your safety. "
            "Think of it as a valuable tool in helping your healthcare team understand your health better."
        ),
        "IRM": (
            "Magnetic Resonance Imaging (MRI) is a remarkable imaging technique that uses magnetic fields and radio waves to create detailed images of the inside of your body. "
            "It is completely safe, as it does not use radiation. The process can be noisy, but the results provide invaluable information for your healthcare provider. "
            "Relax and breathe; the MRI is here to ensure you get the best care possible."
        ),
        "Mammographie": (
            "Mammography is a special type of X-ray designed to look at breast tissue. "
            "It is the most effective way to detect breast cancer early when it is most treatable. "
            "The procedure might feel a little uncomfortable, but it is over quickly and could save your life. "
            "Remember, this is a proactive step in protecting your health and wellbeing."
        ),
        "Echographie": (
            "Ultrasound imaging, or sonography, uses sound waves to produce images of the inside of your body. "
            "It is completely safe, painless, and does not involve any radiation. "
            "Whether you're monitoring a pregnancy or investigating a medical issue, ultrasound is a gentle and effective diagnostic tool. "
            "Rest assured that you are in good hands."
        ),
        "Radiologie interventionnelle": (
            "Interventional radiology involves using imaging techniques like X-rays, CT scans, or MRIs to guide minimally invasive procedures.    "
            "These procedures are often an alternative to surgery, resulting in less pain, quicker recovery, and smaller scars. "
            "It's incredible how modern medicine can treat conditions with such precision and care."
        ),
        "Médecine nucléaire (PET-scan ou TEP-scan, scintigraphie, thérapie)": (
            '''Nuclear medicine is a unique field that uses small amounts of radioactive materials to diagnose and treat diseases.   
            For example, PET scans and scintigraphy provide detailed information about how your body is functioning, rather than just showing its structure.      
            It might sound intimidating, but the procedures are safe, well-controlled, and designed to provide your healthcare team with crucial insights.'''
        )
    }
    return blogs.get(modality, "No blog available for this modality.")

# Streamlit App
st.title("Educational Resources for Medical Imaging")

st.write("Select a medical imaging modality to learn more and ease your worries.")
st.divider()

modality = st.selectbox(
    "Choose a modality:",
    [
        "Radiographie",
        "Scanner",
        "IRM",
        "Mammographie",
        "Echographie",
        "Radiologie interventionnelle",
        "Médecine nucléaire (PET-scan ou TEP-scan, scintigraphie, thérapie)"
    ]
)

if modality:
    st.subheader(f"Learn About {modality}")
    blog = get_blog(modality)
    st.write(blog)
