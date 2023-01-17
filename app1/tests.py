from django.test import TestCase


import requests 
import json

# get method---------
# URL="http://127.0.0.1:8000/apidata/"
# data={}
# jsondata=json.dumps(data)
# def getstdata():
#     data=requests.get(url=URL,data=jsondata)
#     jsdata=data.json()
#     print(jsdata)

# getstdata()





# post method------------
# URL="http://127.0.0.1:8000/apidata/"

# data={"name":"amar singh","age":"33","roll_number":"pata nahi","village":"delhi"}
# jsondata=json.dumps(data)
# def postdata():
#     r=requests.post(url=URL,data=jsondata)
#     jsonres=r.json()
#     print(jsonres)

# postdata()




# put method---------------
# URL="http://127.0.0.1:8000/apidata/"

# data={"id":"1","name":"rai sab","age":"20","roll_number":"1"}
# jsondata=json.dumps(data)
# def updatedata():
#     r=requests.put(url=URL,data=jsondata)
#     jsonres=r.json()
#     print(jsonres)

# updatedata()




# put method---------------
URL="http://127.0.0.1:8000/apidata/"
data={"id":2}
jsondata=json.dumps(data)
def getstdata():
    data=requests.delete(url=URL,data=jsondata)
    jsdata=data.json()
    print(jsdata)

getstdata()

















