import requests
import json
import base64
import io

URL = "http://18.118.161.157:8000/api/patientprofile"
# URL='http://127.0.0.1:8000/api/patientprofile'
data_to_put = {
    # "temp_doc_id":'107',
    # 'username':'Nitin',
    # 'gender':'male',
    # 'age':'34',
    # 'nationality':'Indian',
    # 'smoking_habit':'No',
    # 'diabetes':'No',
    # 'hypertension':'regular',
    # 'obesity':'yes',
    # 'cholesterol':'No',
    # 'previous_illness':'mental balck out',
    # 'family_disease_history':'some syndrom',
    # 'symptoms':'working strers',
    # "user_choice": "appointment",
    # "booking_type": "New Booking",
    "booking_place": "Delhi",
    "booking_hospital":"techno group dama",
    "booking_department": "skin & hear",
    "booking_doctor": "Dr.Mukesh",
    "booking_date": "2021-08-12",
    "booking_time": "16 pm"

}

# this will also store the response if any from the backend server
R = requests.get(url=URL, data=data_to_put)

data = R
print(data)
