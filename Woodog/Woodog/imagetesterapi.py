import requests
import json
import base64
import io

def encoder(img):
    with open(img,"rb") as img:
        encoded_img=base64.b64encode(img.read())
    return encoded_img
mything=encoder("pikachu.jpg")
stream_data=mything

#http://18.118.161.157:8000/

URL="http://127.0.0.1:8000/api/doctorsprofile"
#URL="http://18.118.161.157:8000/api/doctorsprofile"
data_to_put={
    "temp_doc_id":"55",
    "doc_username":"pikachu2",
    "doc_salutation":"Male",
    "doc_email":"somemail@gmail.com",
    "doc_country":"INDIA",
    "doc_city":"Bokaro",
    "doc_degree":"Mbbs",
    "doc_college":" some university ",
    "doc_specialization":"Skinn",
    "doc_regno":"12458762546",
    "doc_image":stream_data,
    "doc_experience_yrs":"2020 passes out bro !",
    "doc_aadhar_card_verif":"646738347389"
}
#changed_tojson=json.dumps(data_to_put) # Changing a Python Object to json here !

R=requests.post(url=URL,data=data_to_put) # this will also store the response if any from the backend server 

data=R
print(data)