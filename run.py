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
    Game welcome message, store user name and return input
    """
    print("""
    Welcome to the Back To The Future Quiz. This quiz is for fans
    of the Back To The Future films.
    Test your knowledge to see if you are a true fan with this fun quiz.
    You can pick from 10, 15 or 20 questions.
    Questions will be mutiple choice,
    there will be 3 answers to choose from A, B or C
    let's start
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
    else:
        print("Time traveller " + name + " Good luck, lets begin!")
    start_game()


# def game_option():
#     """
#     user input to play game, see rules,see ScoreBored
#     """
#     print("Pick from the following options")
#     print("""
#     <         PlayQuiz        >
#     <           Rules         >
#     <        ScoreBoard       >\n
#     Enter 'P' to play game, 'R' to read rules, 'S' for ScoreBoard.""")
    # player_name_input()
    # start_game()


def start_game():
    """
    Adds random question
    """
    for key in quiz_questions:
        print("")
        print(key)
        for i in "question"[quiz_questions - 1]:
            print(i)



# def player_name_input():
#     """
#     gets player name for game
#     """
#     name = input('Enter your name: ')
#     print('Welcome ' + name)


run_game()