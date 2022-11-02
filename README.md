### Date created
2nd Nov 2022

### Project Title
**Medical Insurance Cost Prediction using Logistic Regression & XGBRegressor**

### Description

For this project, we will be building a machine learning model to predict the cost of a medical insureance for an individual based on certain personal details included in the dataset. Our goal is to work through this notebook by collecting data, preprocessing it, splitting it into testing and training datasets, train the model and evaluate the accuracy of our model.

**API**

We have created an API using FastAPI for users to interact with.
You can run the model using uvicorn on your local machine and test the API, refer to medical_insurance_cost_prediction_api.py.

```
uvicorn medical_insurance_cost_prediction_api:app --reload
```

**StreamLit Web App**

We created a simple web app using Streamlit.
You can run the app on your local machine using StreamLit and test the web app, refer to medical_insurance_cost_prediction_webapp.py.

```
streamlit run medical_insurance_cost_prediction_webapp.py
```

The app is deployed on Strealit.io. Use following link to explore: [Medical Insurance Cost Prediction](https://fa1zali-m-webappmedical-insurance-cost-prediction-webapp-fckdze.streamlitapp.com/)

### Files used
We used the following dataset available on Kaggle to work on this project:

* [Medical Cost Personal Datasets](https://www.kaggle.com/datasets/mirichoi0218/insurance)

The datasets consists of some personal details as predictor variables and one target variable. Predictor variables includes the age, gender, bmi, smoker and so on.

### Credits
Thanks to Kaggle for teaching me ML :sparkles: :heart: :sparkles:
