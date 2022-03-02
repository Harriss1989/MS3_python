import gspread
import random
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
    Game start with welcome message and logo
    """
    print("Welcome to the Back To The Future Quiz")
    game_option()


def game_option():
    """
    user input to play game, see rules,see ScoreBored
    """
    print("Pick from the following options")
    print("""
    <         PlayQuiz        >
    <           Rules         >
    <        ScoreBoard       >\n
    Enter 'P' to start game, 'R' to read rules, 'S' for ScoreBoard.""")
    player_name_input()


def player_name_input():
    """
    gets player name for game
    """
    name = input('Enter your name: ')
    print('Welcome ' + name)


run_game()