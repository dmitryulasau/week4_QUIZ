
import time
from begin import *
from questions import *
from random import sample, shuffle




def check_ans(question, ans, questions, score):
    
        
    if ans.lower() == question['answer'].lower():
            
        print(f" + Correct Answer! [ Your score is {score + 1} ]!")
            
        return True
            
    else:
        
        print(f"Wrong Answer :( Correct answer is: {question['answer']} [ Your score is {score} ]")
        
        return False

        
def quiz_game():
                        clear_screen()
                        score = 0
                        print("QUIZ GAME")             
                        questions = 0
                        while questions < 10: 
                            
                            shuffle(quiz)
                            
                            for question in quiz:
                                
                                if questions != 10:
                                    questions += 1
                                    print(f"\n{questions}) {question['question']}") 


                                    answer = input("Your Answer: ")
                                   
                                    check = check_ans(question, answer, questions, score)
                                    if check:
                                        score += 1
                                        
                                        break
                        if score < 3:
                            print(f"\n* Your final score is: {score}! *")
                            print(f"(Your need to listen to Kevin better.)")
                        elif score < 5:
                            print(f"\n* Your final score is: {score}! *")
                            print(f"(Better than nothing.)")
                        elif score < 8:
                            print(f"\n* Your final score is: {score}! *")
                            print(f"(Did you look at the answers?)")
                        elif score <= 10:
                            print(f"\n* Your final score is: {score}! *")
                            print(f"(Elon, is it you?)")

                        repeat = input("\nTake QUIZ again? (Y/N) ")
                        if repeat.lower() == 'y':
                            quiz_game()
                        elif repeat.lower() == 'n':
                            clear_screen()
                            print("Redirecting to the MENU...")
                            time.sleep(2)
                            return
                        else:
                            print("\n /!\ Wrong input! Please follow the instructions /!\ ")
                            time.sleep(1)
                            return

def create_question(payload):
    payload_json_string = json.dumps(payload)
    headers = {
        'Content-Type':'application/json'
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


def main():
    score = 0
    


# LOGIN REGISTRATION PART
    while True:
        clear_screen()
        print("TAKE MY QUIZ")
        print("\n(1) - LOGIN: enter you e-mail")
        print("(2) - REGISTRATION: type 'register' or '2'")
        print("(3) - QUIT: type 'quit' or '3'")
        email = input("\nNew? Register! \nOR \nEnter your email to login: ")
        if email == 'register' or email == '2':
            success_register = register()
            if success_register:
                print("\nRegistration SUCCESSFUL! ✓")
                time.sleep(3)
                continue
        elif email.lower() == "quit" or email == '3':
            clear_screen()
            print("-= Thank you for visiting us! =-")
            break
        else:
            try:
                admin = login(email)['admin']
                
    
                
                time.sleep(1)
            except:
                print("/!\ Invalid Username or Password /!\ ")
                print("\nRedirecting to the MAIN page...")
                time.sleep(3)
                continue
# ADMIN OR REGULAR USER ##################################
        while True:
            
            clear_screen()
# ADMIN PANEL #########################################
            if admin == True:
                print("""
ADMIN PANEL:            
          
(1) Create a question
(X) Edit a question (in progress...)
(X) Delete a quiestion (in progress...)
(4) View ALL questions

(5) Take a QUIZ!

(6) Back to the LOGIN page
   
""")
                option = input("Select your option: ")
                if option == '1':
                    add_question()
                    print("\nYour question was added!")
                    input("\nPress 'ENTER' for MAIN MENU ")
                elif option == '2':
                    pass
                elif option == '3':
                    pass
                elif option == '4':
                    show_all_questions()
                    input("Press 'ENTER' for MAIN MENU ")
                elif option == '5':
                    
                    clear_screen()
                    quiz_game()
                elif option == '6':
                    clear_screen()
                    print("\nRedirecting to the main page...")
                    time.sleep(2)
                    break
                
                else: 
                    clear_screen()
                    print("\n /!\ Wrong input! Please follow the instructions /!\ ")
                    time.sleep(2)
                    continue
            
            else:
# USER MENU #########################################
                while True:
                    clear_screen()
                    print("""
QUIZ MENU:            
          
(1) Take a quiz

(2) Back to the LOGIN page     
""")
                    option = input("Select your option: ")
                    
                    if option == '1':
                        quiz_game()

                    elif option == '2':
                        clear_screen()
                        print("\nRedirecting to the MAIN page...")
                        time.sleep(2)
                        break
                    else: 
                        clear_screen()
                        print("\n /!\ Wrong input! Please follow the instructions /!\ ")
                        time.sleep(1)
                        continue
                break
                


# main()   
