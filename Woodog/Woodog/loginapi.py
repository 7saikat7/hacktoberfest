import requests
import json
import base64
import io

URL='http://127.0.0.1:8000/api/verify'
data_to_put = {
    "phoneNumber":"+9593879456",
    "otp":"845751"
}

R = requests.post(url=URL, data=data_to_put)
