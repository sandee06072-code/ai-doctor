import streamlit as st

# Title
st.title("AI Doctor")

# Symptom selection
st.header("Select Symptoms")

fever = st.checkbox("Fever")
cough = st.checkbox("Cough")
headache = st.checkbox("Headache")

# Predict button
if st.button("Predict Disease"):

    # Example prediction logic
    if fever and cough and headache:
        disease = "Flu"
    elif cough and headache:
        disease = "Cold"
    else:
        disease = "Unknown"

    # Display result
    st.subheader("Possible Disease:")
    st.write(disease)

    # Advice
    st.subheader("Advice:")

    if disease == "Flu":
        st.write("Drink warm fluids and take rest.")
        st.write("Consult a doctor if symptoms continue.")
    elif disease == "Cold":
        st.write("Stay hydrated and rest.")
    else:
        st.write("Please consult a doctor for proper diagnosis.")