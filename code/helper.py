import pandas as pd
import numpy as np

# def preprocess_kaggle(dataset_path):

#     # import the dataset
#     dataset_df = pd.read_csv(dataset_path)

#     # Preprocess
#     dataset_df = dataset_df.apply(lambda col: col.str.strip())

#     test = pd.get_dummies(dataset_df.filter(regex='Symptom'), prefix='', prefix_sep='')
#     test = test.groupby(test.columns, axis=1).agg(np.max)
#     clean_df = pd.merge(test,dataset_df['Disease'], left_index=True, right_index=True)

#     return clean_df

def prepare_symptoms_array(symptoms):
    '''
    Convert a list of symptoms to a ndim(X) (in this case 131) that matches the
    dataframe used to train the machine learning model

    Output:
    - X (np.array) = X values ready as input to ML model to get prediction
    '''
    symptoms_array = np.zeros((1,133))
    df = pd.read_csv('data/clean_dataset.tsv', sep='\t')
    
    for symptom in symptoms:
        symptom_idx = df.columns.get_loc(symptom)
        symptoms_array[0, symptom_idx] = 1

    return symptoms_array