import streamlit as st
from code.DiseaseModel import DiseaseModel
from code.helper import prepare_symptoms_array

# Create disease class and load ML model
disease_model = DiseaseModel()
disease_model.load_xgboost('model/xgboost_model.json')

# Set page width to wide
st.set_page_config(layout='wide')

# Create sidebar
st.sidebar.markdown('# Disease Prediction')
st.sidebar.markdown("This web app uses a machine learning model to predict diseases based on a set of symptoms using Scikit-learn, Python and Streamlit.")
st.sidebar.markdown("Author: Guillermo Chumaceiro")


# Title
st.write('# Disease Prediction using Machine Learning')

symptoms = st.multiselect('What are your symptoms?', options=disease_model.all_symptoms)

X = prepare_symptoms_array(symptoms)

# Trigger XGBoost model
if st.button('Predict'): 
    # Run the model with the python script
    
    prediction, prob = disease_model.predict(X)
    st.write(f'## Disease: {prediction} with {prob*100:.2f}% probability')


    tab1, tab2= st.tabs(["Description", "Precautions"])

    with tab1:
        st.write(disease_model.describe_predicted_disease())

    with tab2:
        precautions = disease_model.predicted_disease_precautions()
        for i in range(4):
            st.write(f'{i+1}. {precautions[i]}')