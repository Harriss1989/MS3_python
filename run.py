import random
import gspread
from google.oauth2.service_account import Credentials
from questions import quiz_questions


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("BTTF_Quiz")

scores = SHEET.worksheet("scores")

data = scores.get_all_values()

# print(data)


def run_game():
    """
    Game welcome message, store user name and return input.
    """
    print("""
    Welcome to the Back To The Future Quiz. This quiz is for fans
    of the Back To The Future films.
    Test your knowledge to see if you are a true fan with this fun quiz.
    You can pick from 10, 15 or 20 questions.
    Questions will be mutiple choice,
    there will be 3 answers to choose from a, b or c
    let's start.
    """)
    name = input("Enter your name time traveller: ")
    name = name.capitalize()
    name = name.strip()
    while len(name) == 0:
        print(" ")
        print("Great Scott! Time traveller, we didn't catch your name")
        print(" ")
        name = input("Enter your name time traveller: ")
        name = name.capitalize()
        name = name.strip()
        print("Time traveller " + name + " Good luck, lets begin!")
    rounds_wanted()


def rounds_wanted():
    """
    Gets player input and selects how many questions are asked for game'
    will give a message if wronge input is entered
    """
    try:
        rounds = input("Pick your amount of questions 10, 15 or 20: ")
        if rounds not in ["10", "20", "30"]:
            raise Exception
        else:
            player_round_pick = int(rounds)
            start_game(player_round_pick)
    except Exception:
        print("Your answer must be either 10, 15 or 20")
        print("no dots, dashes, spaces or letters. Try again")
        


def get_correct_answer(current_question):
    """
    Gets current question and checks for correct answer.
    """
    if current_question["correct"] == current_question["answers"][0]:
        return 'a'
    elif current_question["correct"] == current_question["answers"][1]:
        return 'b'
    elif current_question["correct"] == current_question["answers"][2]:
        return 'c'


def get_player_answer():
    """
    Takes in player input and checks whether answer is correct,
    also gives message if player does not input correctly.
    """
    while True:
        try:
            user_answer = input("Enter Answer: ")
            user_answer = user_answer.lower()
            if user_answer not in ["a", "b", "c"]:
                raise Exception
            else:
                return user_answer
        except Exception:
            print("Your answer must be either a, b or c")
            print("no dots, dashes, spaces or numbers. Try again")


def start_game(rounds_wanted):
    """
    Adds random question
    """
    questions_wanted = rounds_wanted
    questions_list = []
    while len(questions_list) < questions_wanted:
        x = random.randint(0, (len(quiz_questions)-1))
        questions_list.append(quiz_questions[x])
        quiz_questions.pop(x)
    score = 0
    i = 0
    while i < questions_wanted:
        attempts = 1
        print(questions_list[i]["question"])
        print(f"a,{questions_list[i]['answers'][0]}")
        print(f"b,{questions_list[i]['answers'][1]}")
        print(f"c,{questions_list[i]['answers'][2]}")
        correct_answer = get_correct_answer(questions_list[i])

        answer = get_player_answer()
        if answer == correct_answer:
            score += 1
        i += 1
        # when deleting the line below remember to print blank lines
        print(f'your score is {score}\n\n')



run_game()
