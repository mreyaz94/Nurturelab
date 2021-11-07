import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resource(id):
    resp=requests.get(BASE_URL+ENDPOINT+id+'/')
    # if resp.status_code in range(200,300):
    # if resp.status_code==requests.codes.ok:
    print(resp.status_code)
    print(resp.json()) # json() to convert in python dicyionary.
    # else:
    #     print('Some thing goes wrong')

def get_all():
    resp=requests.get(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json()) # To get data
# get_all()

def user_register():
    new_emp={
    'first_name':"AAFFAN",
    'email':'affan@gmail.com',
    'username':'ssss2',
    'password':'ansari',
    }
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp)) #python dict convert to json data
    print(resp.status_code)
    print(resp.json())
user_register()

def user_login(id):
    new_emp={
    'eno':5,
    'esal':7000,
    'eaddr':'Delhi'
    }
    resp=requests.put(BASE_URL+ENDPOINT+str(id)+'/',data=new_emp) #python dict convert to json data
    print(resp.status_code)
    print(resp.json())

def delete_resource(id):
    resp=requests.delete(BASE_URL+ENDPOINT+str(id)+'/') #python dict convert to json data
    print(resp.status_code)
    print(resp.json())

# delete_resource(5)
# update_resource(4)
# user_register()   --done
# get_resource('4')
# get_ all()        --done
