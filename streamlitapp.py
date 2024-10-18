import pickle
import streamlit as st

# Loading the saved models
parkinsons_model = pickle.load(open('parkinson_model.sav', 'rb'))

# Page title
st.title("Parkinson's Disease Prediction using ML")

# Adding CSS styles for a more attractive layout
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://raw.githubusercontent.com/SHAIK-RAIYAN-2022-CSE/malaria/main/Images-free-abstract-minimalist-wallpaper-HD.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(0, 0, 0, 0);
}
.block-container {
    background: rgba(0, 0, 0, 0.7);
    padding: 40px;
    border-radius: 20px;
    max-width: 900px;
    margin: auto;
    backdrop-filter: blur(15px);
    box-shadow: 0px 6px 24px rgba(0, 0, 0, 0.8);
}
h1, h2, h3, h4, h5, h6, p {
    color: #FF6347;
    text-align: center;
    font-family: 'Arial', sans-serif;
}
.stTextInput {
    background-color: rgba(255, 255, 255, 0.9);
    border: 2px solid #FF6347;
    border-radius: 8px;
    padding: 10px;
}
.stButton>button {
    background-color: #FF6347;
    color: white;
    font-size: 20px;
    padding: 12px 30px;
    border-radius: 10px;
    border: none;
    transition: 0.3s;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}
.stButton>button:hover {
    background-color: white;
    color: #FF6347;
    border: 2px solid #FF6347;
}
.success-message {
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    color: #32CD32; /* Lime Green */
}
</style>
""", unsafe_allow_html=True)

# Input fields in columns
col1, col2, col3, col4, col5 = st.columns(5)

# List of input field labels
inputs = [
    'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 
    'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP', 
    'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 
    'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5', 
    'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 
    'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
]

# Create text inputs dynamically
input_values = {}
for i, label in enumerate(inputs):
    col = [col1, col2, col3, col4, col5][i % 5]
    input_values[label] = col.text_input(label, key=label, help="Enter a numerical value")

# Prediction logic
parkinsons_diagnosis = ''

# Creating a button for Prediction    
if st.button("Parkinson's Test Result"):
    try:
        input_data = [float(input_values[label]) for label in inputs]
        parkinsons_prediction = parkinsons_model.predict([input_data])
        
        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
    except ValueError:
        parkinsons_diagnosis = "Please enter valid numerical values in all fields."

# Display the result with styling
if parkinsons_diagnosis:
    st.markdown(f"<p class='success-message'>{parkinsons_diagnosis}</p>", unsafe_allow_html=True)
