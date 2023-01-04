 
# Importing the necessary function
import pickle
import streamlit as st
 
# Loading the trained model
pickle_in = open('tuned_lr_Model.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
# Making sure the model can make a prediction and give output without crashing
@st.cache()
  
# Defining a function which will take user inputs, pre-process the user inputs, and make a prediction of whether the patient has kidney disease
def prediction(Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio):   
    # Pre-processing user input    
    if Gender == "Female":
        Gender = 0
    else:
        Gender = 1   
    # Making predictions 
    prediction = classifier.predict([[Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]]) 
    if prediction == 0:
        pred = 'Liver Disease not detected'
    else:
        pred = 'Liver Disease detected'
    return pred
       
# Creating a function to create the GUI (Graphical User Interface), take the user input, processing the user input, and displaying the prediction on the screen
def main():       
    # Creating the frontend elements of the website 
    html_temp = """ 
    <div style ="background-color:red;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Liver Disease Predictor</h1> 
    </div> 
    """
    # Displaying the frontend aspect
    st.markdown(html_temp, unsafe_allow_html = True)   
    # Creating boxes to ask the user for the input
    Gender = st.selectbox('Gender',("Female","Male")) 
    Age = st.number_input( "Age" )
    Total_Bilirubin = st.number_input( "Total Bilirubin" )
    Direct_Bilirubin = st.number_input( "Direct Bilirubin" )
    Alkaline_Phosphotase = st.number_input( "Alkaline Phosphotase" )
    Alamine_Aminotransferase = st.number_input( "Alamine Aminotransferase" )
    Aspartate_Aminotransferase = st.number_input( "Aspartate Aminotransferase" )
    Total_Protiens = st.number_input( "Total Protiens" )
    Albumin = st.number_input( "Albumin" )
    Albumin_and_Globulin_Ratio = st.number_input( "Albumin and Globulin_Ratio" )
    result =""
    # Creating a predict button to create a prediction and store the prediction
    if st.button("Predict"): 
        result = prediction(Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio) 
        st.success('Report Results: {}'.format(result))
            
if __name__=='__main__': 
    main()
