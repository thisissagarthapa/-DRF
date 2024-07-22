import requests
import json
URL='http://127.0.0.1:8000/stuinfo/'
def get_id(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    headers={
        "Content-Type":"application/json"
        }
    r=requests.get(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# get_id(1)

def post_data():
    data={
        "name":"suman",
        "age":35,
        "email":"suman@gamil.com"
    }

    json_data=json.dumps(data)
    headers={
        "Content-Type":"application/json"
        }
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# post_data()


def update_data():
    data={
        "id":7,
        "name":"saurav",
        "age":24,
        "email":"saurav@gamil.com"
    }

    json_data=json.dumps(data)
    headers={
        "Content-Type":"application/json"
        }   
    r=requests.put(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# update_data()


def delete_data():
    data={"id":7,}
    json_data=json.dumps(data)
    headers={
        "Content-Type":"application/json"
        }    
    r=requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# delete_data()
