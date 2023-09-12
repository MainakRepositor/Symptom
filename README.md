# Project

A streamlit app that uses a machine learning model to predict disease based on list of symptoms

## Installation

This repository contains three ways to setup the environments and run the app.

### Easiest: docker

1. If you have docker install, just run

```
docker run -p 8501:8501 guillechuma/disease_pred_streamlit
```

2. See the app at <https://localhost:8501>

### Easiest: conda

1. Run this command

```
conda env create -f environment.yml
```

### Easy: pip

1. Run this command inside python environment

```
pip install -r requirements.txt
```

## How-to

1. Clone repository locally
2. Create and activate conda/python environment as specified above.
3. inside the project folder, run

```
streamlit run app.py
```

Enjoy!

## Data Source

https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset

## Author

Guillermo Chumaceiro