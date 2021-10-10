import requests
import json
import base64
import io

def encoder(img):
    with open(img,'rb') as img:
        encoded_img=base64.b64encode(img.read())
    return encoded_img
mything=encoder('teresa.png')
stream_data=mything



URL="http://127.0.0.1:8000/api/testimage"
data_to_put={
    "check2":"2",
    #'Image':stream_data,
    "Image":''
    # 'temp_doc_id':'2' ,
    # 'name_of_doctor': 'Dr.Mukhersh Sing Rana',
    # 'gender':'Male',
    # 'email':'somemail@gmail.com',
    # 'country':'INDIA',
    # 'city':'Bokaro',
    # 'degree':'Mbbs',
    # 'college_name':' some university ',
    # 'specilisation':'Skinn',
    # 'registration_no':'12458762546',
    # 'profile_picture':stream_data,
    # 'salutation':'Mr.DOC',
    # 'experience':'2020 passes out bro !',
    # 'adhar_card':'646738347389',
}
#changed_tojson=json.dumps(data_to_put) # Changing a Python Object to json here !

R=requests.post(url=URL,data=data_to_put) # this will also store the response if any from the backend server 

data=R
print(data)