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

# def run_game():
#     """
#     Game start with welcome message and logo
#     """
#     print("Welcome to the Back To The Future Quiz")
#     print("▒▒h       
#                                           ,╓╓╓╓╓╓╓╓╓╓╓╓▒▒▒▒╓m$ÖÖQⁿ═w, ,▒▀Ç ,▄█████
#                                      ,▄╗╢▒▄███████████▌▒▒▒▌▒█▒▒@▒▒▒▒╢╢▒████████░░█▌
#                                  ▄mÑ▒▄████████████████▌▒▒▒█▒████▓██▓▓▓╬▓▒▒▒▀▀▀████▌
#                      ,,,╓╓╖╥╖╥R▒▒▒▒███▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▀▒▒▒▒▒░█
#        ,╓╗@@@╣╢╢▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒[
#       ╓░░▒▒▒@▒▒▒░█████████░▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀░█████████░▀▒▒▒▒▒▒▒███
#      ┌╢▒▒╣█▒@█▒░███▓▓▓▓▓███▌║▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╢╢╢╢╢╢╜░██▀▓▓▓▓▓███▌║▒▒▒▄████▀
#         ████▄▄▄██▌╢╣»è⌐╢╣███▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄██▌╣╣»è⌐╢╣███▄███████r
#        ▀▀▀▀▀▀▀▀▀▀█▓╣▓▓▓╣▓█████████████████████████████████████▓╣▓▓▓╣▓███▀▀` ▀'
#                  ▀▀███████▀                                 ▀███████▀▀")


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

def player_input_selection():
    """
    Checks for player input and validates input is correct
    """
    selection = input('P, R, S')
    try:
       while True:
               if selection.upper() in ['P', 'R', 'S']:
                return selection
               else:
                   print("Invalid selection please try again P, R, S")
                   selection = input('P, R, S')


player_input_selection()

# def game_loop():
#     “”"
#     runs the main game and takes in data needed for game
#     “”"
#     name = get_player_name()
# def get_player_name():
#     “”"
#     gets player name input displays to terminal
#     shows error message if name too long
#     “”"
#     print(“Enter your name: “)
#     x = input(“”)