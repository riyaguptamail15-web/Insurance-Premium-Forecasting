from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
import json


class Patient(BaseModel):
    id: str = Field(..., description='Patient ID')
    name: str = Field(..., description='Patient name')
    city: str = Field(..., description='City of residence')
    age: int = Field(..., ge=0, description='Patient age')
    gender: str = Field(..., description='Gender of the patient')
    height: float = Field(..., gt=0, description='Height in meters')
    weight: float = Field(..., gt=0, description='Weight in kg')
    bmi: float = Field(..., ge=0, description='Body mass index')
    verdict: str = Field(..., description='Health verdict')


app = FastAPI()

#decorator ki help se home route create kiya 
@app.get("/")
def hello():
    return{'message':'Hello World'}
              # get request sent when server se kuch data fetch karna chahte ho 
              # post request when server par data bhejna chahte ho
              # The / is the URL of the website you want to hit, lets says campus.in so it hits on campus.in/


def load_data():
    with open ('patients.json', 'r') as f:
        data=json.load(f)
        return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f, indent=2)
    
#function banaya

# running on local host, not deployed

#uvicorn main:app --reload means that its strating a server on uvicorn which will send HTTP request

@app.get('/about')# a new endpoit created where when the user types/about, he gets redirected to about page 
def about():
    return {'message': 'ÇampusX is an eductaion platform where you can learn AI'}

@app.get('/view')
def view():
    data=load_data()
    return data

#reload used therefore dont have to manually reload website again, web server automatically updates.

@app.get('/patient/{patient_id}') 
def view_patient(patient_id:str=Path(..., description='ID of the patient in the DB', examples='P001')):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')

@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of height, weight or bmi."),
    order: str = Query("asc", description="Sort in asc or desc order")
):
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field. Select from {valid_fields}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Select order between asc or desc"
        )

    data = load_data()

    sort_order = True if order == "desc" else False

    sorted_order = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order
    )

    return sorted_order   

@app.post('/create')
def create_patient(patient:Patient):
    data=load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')
    data[patient.id]=patient.model_dump(exclude=['id'])
    
    save_data(data)
    return JSONResponse(status_code=201, content={'message':'Patient created succesfully'})
                                                                                                                      
                                                                                        
                                                                                        
