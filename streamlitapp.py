import pickle
import streamlit as st

# Loading the saved model
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
input {
    background-color: white !important; /* Set input background to white */
    color: black !important; /* Set input text color to black */
    border: 1px solid #FF6347; /* Border color */
    border-radius: 5px; /* Rounded corners */
    padding: 10px; /* Padding inside the input box */
}
</style>
""", unsafe_allow_html=True)

# Input fields in columns
col1, col2, col3 = st.columns(3)

# Grouping inputs for each column
input_groups = [
    # Column 1
    [
        ('MDVP:Fo(Hz)', 150.0, 0.0, 300.0, 0.1),
        ('MDVP:Fhi(Hz)', 200.0, 0.0, 300.0, 0.1),
        ('MDVP:Flo(Hz)', 100.0, 0.0, 300.0, 0.1),
        ('MDVP:Jitter(%)', 0.5, 0.0, 5.0, 0.01),
        ('MDVP:Jitter(Abs)', 0.002, 0.0, 0.1, 0.0001),
        ('DFA', 0.5, 0.0, 1.0, 0.01),
        ('spread1', 0.5, 0.0, 1.0, 0.01),
        ('spread2', 0.5, 0.0, 1.0, 0.01),
    ],
    # Column 2
    [
        ('MDVP:RAP', 0.3, 0.0, 1.0, 0.01),
        ('MDVP:PPQ', 0.4, 0.0, 1.0, 0.01),
        ('Jitter:DDP', 0.1, 0.0, 1.0, 0.01),
        ('MDVP:Shimmer', 0.5, 0.0, 1.0, 0.01),
        ('MDVP:Shimmer(dB)', 0.2, 0.0, 1.0, 0.01),
        ('D2', 2.0, 0.0, 5.0, 0.1),
        ('PPE', 0.5, 0.0, 1.0, 0.01)
    ],
    # Column 3
    [
        ('Shimmer:APQ3', 0.3, 0.0, 1.0, 0.01),
        ('Shimmer:APQ5', 0.4, 0.0, 1.0, 0.01),
        ('MDVP:APQ', 0.5, 0.0, 1.0, 0.01),
        ('Shimmer:DDA', 0.3, 0.0, 1.0, 0.01),
        ('NHR', 0.2, 0.0, 1.0, 0.01),
        ('HNR', 20.0, 0.0, 50.0, 0.1),
        ('RPDE', 0.3, 0.0, 1.0, 0.01),
        

    ]
]

# Create text inputs dynamically and distribute them across the columns
input_values = {}

for idx, group in enumerate(input_groups):
    col = [col1, col2, col3][idx]
    for label, default, min_val, max_val, step in group:
        input_values[label] = col.number_input(label, value=default, min_value=min_val, max_value=max_val, step=step)

# Prediction logic
parkinsons_diagnosis = ''

# Creating a button for Prediction    
if st.button("Parkinson's Test Result"):
    try:
        # Ensure we use the correct keys from input_values
        input_data = [float(input_values[label]) for label in input_values]
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
