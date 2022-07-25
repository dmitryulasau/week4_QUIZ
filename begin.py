import requests

url = 'https://cae-bootstore.herokuapp.com/'

endpoint_login = '/login'
endpoint_user = '/user'

endpoint_question = '/question'
endpoint_question_all = '/question/all'

def get_questions():
    questions = requests.get(url + endpoint_question_all)
    return questions.json()['questions']

quiz = get_questions()

quiz

def show_all_questions():
    clear_screen()
    for question in quiz:
        print(f"QUESTION: {question['question']}")
        print(f"ANSWER: {question['answer']}")
        print(f"AUTHOR: {question['author']}")
        print(f"ID: {question['id']}\n")
          

# REGISTER A USER
import json

def register_user(payload):
    payload_json_string = json.dumps(payload)
    headers = {
        'Content-Type':'application/json'
    }
    response = requests.post(
        url + endpoint_user,
        data = payload_json_string,
        headers = headers
    )
    return response.text

import base64

def login_user(user_name, password):
    auth_string = user_name + ":" + password
    
    headers={
        'Authorization' : "Basic "+base64.b64encode(auth_string.encode()).decode()
    }
    
    user_data = requests.get(
        url + endpoint_login,
        headers=headers
    )
    print(f"Hello, {user_data.json()['first_name'].title()}!")

    admin = user_data.json()['admin']
    if admin == True:
        print(f"\n* ADMINISTRATOR *")
    else:
        print(f"\n* USER *")
    
    return user_data.json()

def edit_user(token, payload):
    payload_json_string = json.dumps(payload)
    headers={
        'Content-Type':'application/json',
        'Authorization':'Bearer ' + token
    }
    response = requests.put(
        url + endpoint_user,
        data=payload_json_string,
        headers=headers
    )
    return response.text

def delete_user(token):
    headers = {
        'Authorization':"Bearer " + token
    }
    
    response = requests.delete(
        url+endpoint_user,
        headers=headers
    )
    return response.text


import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# LOGIN REGISTER
from getpass import getpass

def login(email):
    clear_screen()
    password = getpass("Password: ")
    clear_screen()
    user = login_user(email, password) 
    return user

def register():
    clear_screen()
    print("REGISTRATION:")
    email = input("\nEmail: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    password = getpass("Password: ")
    
    
    user_dict={
        "email":email,
        "first_name":first_name,
        "last_name":last_name,
        "password":password
    }
    return register_user(user_dict)