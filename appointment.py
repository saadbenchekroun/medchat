import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import random

# Sample data for doctors (you would typically fetch this from a database)
doctors_data = {
    'Name': [
        'Dr. Smith', 'Dr. Johnson', 'Dr. Lee', 'Dr. Brown', 
        'Dr. El Amrani', 'Dr. Ait Taleb', 'Dr. Bouazza', 'Dr. Jebari', 'Dr. Hakam', 
        'Dr. Lahlou', 'Dr. Bennis', 'Dr. Rachidi', 'Dr. Fassi', 'Dr. Tazi'
    ],
    'Specialty': [
        'Radiographie', 'Scanner', 'IRM', 'Mammographie',
        'Echographie', 'Radiologie interventionnelle', 'Médecine nucléaire',
        'Radiographie', 'Scanner', 'IRM', 'Mammographie', 'Echographie', 
        'Radiologie interventionnelle', 'Médecine nucléaire'
    ],
    'Latitude': [
        48.8566, 48.8567, 48.8568, 48.8569, 
        34.0331, 34.0332, 34.0333, 34.0334, 
        34.0335, 34.0336, 34.0337, 34.0338, 
        34.0339, 34.0340
    ],
    'Longitude': [
        2.3522, 2.3523, 2.3524, 2.3525, 
        -4.9998, -4.9997, -4.9996, -4.9995, 
        -4.9994, -4.9993, -4.9992, -4.9991, 
        -4.9990, -4.9989
    ]
}

# Create a DataFrame
df = pd.DataFrame(doctors_data)

# User selects a medical imaging type
imaging_types = [
    "Radiographie",
    "Scanner",
    "IRM",
    "Mammographie",
    "Echographie",
    "Radiologie interventionnelle",
    "Médecine nucléaire"
]

selected_type = st.selectbox("Select Imaging Type", imaging_types)

# Filter doctors based on selection
filtered_doctors = df[df['Specialty'] == selected_type]

# Create a map centered around the first doctor's location or default location
if not filtered_doctors.empty:
    lat = filtered_doctors['Latitude'].mean()
    lon = filtered_doctors['Longitude'].mean()
    m = folium.Map(location=[lat, lon], zoom_start=12)

    # Add markers for each doctor
    for _, row in filtered_doctors.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Name'],
            tooltip=row['Specialty']
        ).add_to(m)

    # Display the map in Streamlit
    st_folium(m, width=2000, height=300)

    # Show the list of doctors on the right side
    st.write("### Nearby Doctors")
    st.dataframe(filtered_doctors[['Name', 'Specialty']])
else:
    st.write("No doctors found for the selected specialty.")