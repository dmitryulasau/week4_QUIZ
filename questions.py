from begin import clear_screen
import requests
from begin import *
from quiz import *

def create_question(token, payload):
    payload_json_string = json.dumps(payload)
    headers={
        'Content-Type':'application/json',
        'Authorization':'Bearer ' + token
    }
    response = requests.post(
        url + endpoint_question,
        data = payload_json_string,
        headers = headers
    )
    return response.text

def add_question():
    clear_screen()
    print("ADD A QUESTION: ")
    question = input("\nQUESTION: ")
    answer = input("ANSWER: ")

    question_dict={
        "question": question,
        "answer": answer, 
    }

    return create_question(question_dict)