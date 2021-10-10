import requests
import json

URL="http://127.0.0.1:8000/api/doctorschedule"
data_to_put={
    "doctor_id":"12",

    "monday":"monday",
    "m_startime":"16:30:00",
    "m_endtime":"17:30",
   
    "tuesday":"tuesday",
    "t_starttime":"16:30:00",
    "t_endtime":"17:30:00",

    "wednesday":"wednesday",
    "w_starttime":"16:30:30",
    "w_endtime":"17:30",

    "thrusday":"Thrusday",
    "th_starttime":"16:30:30",
    "th_endtime":"16:30:30",

    "friday":"friday",
    "f_starttime":"16:30:30",
    "f_endtime":"16:30:30",
    
    "saturday":"saturday",
    "s_starttime":"16:30:30",
    "s_endtime":"16:30:30",
    
    "sunday":"sunday",
    "su_starttime":"16:30:30",
    "su_endtime":"16:30:30",
    
    "time_per_session":"20",
    "total_sessions":"3"

}
R = requests.post(url=URL, data=data_to_put)
