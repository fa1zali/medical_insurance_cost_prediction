from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import pickle
import json
import numpy as np

app = FastAPI()

model = pickle.load(open('../saved_model/medical_insurance_model.sav', 'rb'))

class Gender(int,Enum):
    
    female = 0
    male = 1

class Smoker(int,Enum):
    
    No = 0
    Yes = 1

class Region(int, Enum):

    northeast = 0
    northwest = 1
    southeast = 2
    southwest = 3

class IndividualDetails(BaseModel):

    age : int
    sex : Gender
    bmi : float
    children : int
    smoker : Smoker
    region : Region


@app.post("/get_insurance_cost")
def get_insurance_cost(input_parameters:IndividualDetails):
    input_data = input_parameters.json()
    input_dct = json.loads(input_data)

    a = input_dct["age"]
    b = input_dct["sex"]
    c = input_dct["bmi"]
    d = input_dct["children"]
    e = input_dct["smoker"]
    f = input_dct["region"]

    input_list = [a,b,c,d,e,f]
    input_data_arr = np.asarray(input_list)
    input_data_reshaped = input_data_arr.reshape(1, -1)

    cost = model.predict(input_data_reshaped)
    
    return {'cost' : float(cost[0])}