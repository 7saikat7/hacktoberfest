import requests
import json
import base64
import io

#URL = "http://18.118.161.157:8000/api/patientdemographic"
URL='http://127.0.0.1:8000/api/patientdemographic'
data_to_put = {
    "temp_patient_id": "17",
    "username": "Nitin",
    "gender": "male",
    "age": "34",
    "nationality": "Indian",
    "smoking_habit": "No",
    "diabetes": "No",
    "hypertension": "regular",
    "obesity": "yes",
    "cholesterol": "No",
    "previous_illness": "mental balck out",
    "family_disease_history": "some syndrom",
    "symptoms": "working strers"
}

# Changing a Python Object to json here !
changed_tojson = json.dumps(data_to_put)
# this will also store the response if any from the backend server
R = requests.post(url=URL, data=data_to_put)

data = R
print(data)
