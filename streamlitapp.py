import pickle
import streamlit as st

# Loading the saved models
parkinsons_model = pickle.load(open('parkinson_model.sav', 'rb'))

# Page title
st.title("Parkinson's Disease Prediction using ML")

# Adding CSS styles
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
    padding: 30px;
    border-radius: 15px;
    max-width: 800px;
    margin: auto;
    backdrop-filter: blur(10px);
    box-shadow: 0px 6px 24px rgba(0, 0, 0, 0.8);
}
.stButton>button {
    background-color: #FF6347;
    color: white;
    font-size: 18px;
    padding: 12px 28px;
    border-radius: 10px;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: white;
    color: #FF6347;
    border: 2px solid #FF6347;
}
h1, h2, h3, h4, h5, h6, p {
    color: white;
    text-align: center;
}
.text-input {
    background-color: rgba(255, 255, 255, 1);
    border: 1px solid #FF6347;
    border-radius: 5px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# Input fields in columns
col1, col2, col3, col4, col5 = st.columns(5)

# List of input labels and their default values
inputs = [
    ('MDVP:Fo(Hz)', '150.0'), ('MDVP:Fhi(Hz)', '200.0'), 
    ('MDVP:Flo(Hz)', '100.0'), ('MDVP:Jitter(%)', '0.5'), 
    ('MDVP:Jitter(Abs)', '0.002'), ('MDVP:RAP', '0.3'), 
    ('MDVP:PPQ', '0.4'), ('Jitter:DDP', '0.1'), 
    ('MDVP:Shimmer', '0.5'), ('MDVP:Shimmer(dB)', '0.2'), 
    ('Shimmer:APQ3', '0.3'), ('Shimmer:APQ5', '0.4'), 
    ('MDVP:APQ', '0.5'), ('Shimmer:DDA', '0.3'), 
    ('NHR', '0.2'), ('HNR', '20.0'), 
    ('RPDE', '0.3'), ('DFA', '0.5'), 
    ('spread1', '0.5'), ('spread2', '0.5'), 
    ('D2', '2.0'), ('PPE', '0.5')
]

# Create text inputs dynamically with default values
input_values = {}
for i, (label, default) in enumerate(inputs):
    col = [col1, col2, col3, col4, col5][i % 5]
    input_values[label] = col.text_input(label, key=label, value=default)

# Prediction logic
parkinsons_diagnosis = ''

# Creating a button for Prediction    
if st.button("Parkinson's Test Result"):
    try:
        # Ensure we use the correct keys from input_values
        input_data = [float(input_values[label]) for label, _ in inputs]
        parkinsons_prediction = parkinsons_model.predict([input_data])                          
        
        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
    except ValueError:
        parkinsons_diagnosis = "Please enter valid numerical values in all fields."
    except KeyError as e:
        parkinsons_diagnosis = f"Error: Missing input value for {e}."

# Display the result
if parkinsons_diagnosis:
    st.success(parkinsons_diagnosis)
