import random
import os
import gspread
import time
from google.oauth2.service_account import Credentials
from questions import quiz_questions


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Accesses the excel sheet itself
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("BTTF_Quiz")


class C:
    """
    Class to hold color variables.
    """
    RESET = '\33[0m'
    RED = '\33[31m'
    GOLD = '\33[93m'
    SILVER = '\33[2m'
    GREEN = '\33[32m'
    BLUE = '\33[34m'


def clear_screen():
    """
    Clears Screen prior to new content.
    Original code from
    http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf
    Recommended to me by Matt Bodden
    https://github.com/MattBCoding
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def run_game():
    """
    Game welcome message calls main menu function.
    """
    print("""
    Welcome to the Back To The Future Quiz. This quiz is for fans
    of the Back To The Future films.
    Test your knowledge to see if you are a true fan with this fun quiz.
    You can pick from 10, 15 or 20 questions.
    Questions will be mutiple choice,
    there will be 3 answers to choose from a, b or c.
    Will you score enough pionts to be featured on the leaderboard?
    let's start.\n
    """)
    main_menu()


def main_menu():
    """
    Give player two options to choose from, start game or view leaderboard
    """
    print("1- Start Game\n")
    print("2- Leaderboard\n")
    while True:
        try:
            pick_one = input("please select an option 1 or 2:\n")
            if pick_one not in ["1", "2"]:
                raise Exception
            else:
                break
        except Exception:
            print("Your answer must be either 1 or 2:")
            print("No dots, dashes, spaces or letters. Try again!")

    if pick_one == "1":
        get_name()
    elif pick_one == "2":
        score_board()


def get_name():
    """
    Store user name and check for only letters no other characters.
    """
    try:
        while True:
            name = input("Enter your name Time Traveller: \n")
            name = name.capitalize()
            name = name.strip()
            if len(name) <= 15 and name.isalpha():
                print("Time Traveller " + name + " Good luck, lets begin!\n")
                break
            else:
                print("Great Scott! Time traveller, we didn't catch your name")
                print("No dots, dashes, spaces or numbers. Try again!")
    except Exception:
        clear_screen()

    rounds_wanted(name)


def score_board():
    """
    Gets the value of scores from worksheets and displays
    leaderboard to player
    """
    worksheet_ten = SHEET.worksheet("10").get_all_values()
    sorted_ten = []
    for sub_list in worksheet_ten:
        sub_list[1] = int(sub_list[1])
        sorted_ten.append(sub_list)
    worksheet_ten = sorted(sorted_ten, key=lambda x: x[1], reverse=True)

    worksheet_fifteen = SHEET.worksheet("15").get_all_values()
    sorted_fifteen = []
    for sub_list in worksheet_fifteen:
        sub_list[1] = int(sub_list[1])
        sorted_fifteen.append(sub_list)
    worksheet_fifteen = sorted(sorted_fifteen,
                               key=lambda x: x[1], reverse=True)

    worksheet_twenty = SHEET.worksheet("20").get_all_values()
    sorted_twenty = []
    for sub_list in worksheet_twenty:
        sub_list[1] = int(sub_list[1])
        sorted_twenty.append(sub_list)
    worksheet_twenty = sorted(sorted_twenty, key=lambda x: x[1], reverse=True)

    print(f"{C.BLUE}Leaderboard{C.RESET}\n")
    print("10 rounds")
    print(f'{C.GOLD}1st{C.RESET} - {worksheet_ten[0][0]} with \
{C.BLUE}{worksheet_ten[0][1]}{C.RESET} pts')
    print(f'{C.SILVER}2nd{C.RESET} - {worksheet_ten[1][0]} with \
{C.BLUE}{worksheet_ten[1][1]}{C.RESET} pts')
    print(f'{C.RED}3rd{C.RESET} - {worksheet_ten[2][0]} with \
{C.BLUE}{worksheet_ten[2][1]}{C.RESET} pts\n')
    print("15 rounds")
    print(f'{C.GOLD}1st {C.RESET} - {worksheet_fifteen[0][0]} with \
{C.BLUE}{worksheet_fifteen[0][1]}{C.RESET} pts')
    print(f'{C.SILVER}2nd {C.RESET} - {worksheet_fifteen[1][0]} with \
{C.BLUE}{worksheet_fifteen[1][1]}{C.RESET} pts')
    print(f'{C.RED}3rd {C.RESET} - {worksheet_fifteen[2][0]} with \
{C.BLUE}{worksheet_fifteen[2][1]}{C.RESET} pts\n')
    print("20 rounds")
    print(f'{C.GOLD}1st {C.RESET} - {worksheet_twenty[0][0]} with \
{C.BLUE}{worksheet_twenty[0][1]}{C.RESET} pts')
    print(f'{C.SILVER}2nd {C.RESET} - {worksheet_twenty[1][0]} with \
{C.BLUE}{worksheet_twenty[1][1]}{C.RESET} pts')
    print(f'{C.RED}3rd {C.RESET} - {worksheet_twenty[2][0]} with \
{C.BLUE}{worksheet_twenty[2][1]}{C.RESET} pts\n')
    main_menu()


def rounds_wanted(name):
    """
    Gets player input and selects how many questions are asked for game'
    will give a message if wronge input is entered
    """
    player_round_pick = 0
    while True:
        try:
            rounds = input("Pick your amount of questions 10, 15 or 20: \n")
            if rounds not in ["10", "15", "20"]:
                raise Exception
            else:
                player_round_pick = int(rounds)
                clear_screen()
                break
        except Exception:
            print("Your answer must be either 10, 15 or 20")
            print("no dots, dashes, spaces or letters. Try again")

    start_game(player_round_pick, name)


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


def start_game(rounds_wanted, name):
    """
    Adds random question to game , updates player scor and tells them
    if question is right or wrong.
    """
    questions_wanted = rounds_wanted
    questions_list = []
    quiz_questions_list = quiz_questions.copy()
    while len(questions_list) < questions_wanted:
        x = random.randint(0, (len(quiz_questions_list)-1))
        questions_list.append(quiz_questions_list[x])
        quiz_questions_list.pop(x)
    score = 0
    i = 0
    while i < questions_wanted:
        print(questions_list[i]["question"])
        print(f"a) {questions_list[i]['answers'][0]}\n")
        print(f"b) {questions_list[i]['answers'][1]}\n")
        print(f"c) {questions_list[i]['answers'][2]}\n\n")
        correct_answer = get_correct_answer(questions_list[i])
        answer = get_player_answer()
        if answer == correct_answer:
            score += 1
            print(f'{C.GREEN}Correct{C.RESET} good job\n')
        else:
            print(f'That is {C.RED}Incorrect{C.RESET} on to the next Question')
        i += 1
        print(f'Your score is {C.GOLD}{score}{C.RESET}\n\n')
        time.sleep(2)
        clear_screen()
    end_game(score, questions_wanted, name)


def end_game(score, questions_wanted, name):
    """
    Get player score and displays depending on rounds picked how much they
    scored with an option to play again,
    updates google sheet with player name and score for leaderbored
    """
    if questions_wanted == 10:
        sheet_ten = SHEET.worksheet("10")
        sheet_ten.append_row([name, score])
        # get score sheet 10 and update with name and score
    elif questions_wanted == 15:
        sheet_fifteen = SHEET.worksheet("15")
        sheet_fifteen.append_row([name, score])
        # get score sheet 15 and update with name and score
    else:
        sheet_twenty = SHEET.worksheet("20")
        sheet_twenty.append_row([name, score])
        # get score sheet 20 and update with name and score
    clear_screen()
    print(f'Congratulations {name} you scored {score}\n')
    play_again(name)


def play_again(name):
    """
    Gives the player the option to play again
    """
    print(f'Would you like you play again {name}?\n')
    print('Type y for yes or n for no\n')
    while True:
        try:
            user_answer = input("Enter Answer: ")
            user_answer = user_answer.lower()
            if user_answer not in ["y", "n"]:
                raise Exception
            else:
                break
        except Exception:
            print("Your answer must be either y, n")
            print("No dots, dashes, spaces or numbers. Try again")
    if user_answer == "y":
        restart_game(name)
    else:
        exit_game(name)


def restart_game(name):
    """
    Restart's game and give player option to change question amount
    """
    print(f"{name} Why not try a different amount of questions.\n")
    rounds_wanted(name)


def exit_game(name):
    """
    Ends game prints goodbye message
    """
    print(f"\n Thank you for playing {name}")
    print("To play again press the big blue button.\n")
    print("\n Goodbye Time Traveler")


run_game()
