# Back to the Future Quiz (MS3_python)
## Introduction
Back to the Future Quiz (MS3_python) is a browser-based game built in Python. It is a fun quiz game focusing on the Back to The Future movie franchise, and also my favourite movie of all time.

This game utilises the Code Institute Python template, as it was developed in Python for use in the terminal. This makes it available within a web browser.

![Game image](/assets/images/main.png)

[Link to live site](https://back-to-the-future-quiz.herokuapp.com/) If you would like to open this document in a new browser tab, please press CTRL + Click.

# UX
## The Strategy Plane
* Back To the Future quiz game is designed to be a fun quiz for fans of the Back to The Future movie, players can challenge themselves on their trivia knowledge from the movie and test themselves on what they can remember. Player scores will be recorded in a spreadsheet and the top 3 will be displayed in the terminal. There is the option to choose the number of questions played, either 10, 15 or 20 depending on how challenging the player would like the quiz to be.

## Site Goals
* To provide users and die-hard fans of the movie, with a fun and simple to play quiz.
* To provide users and die-hard fans of the movie, the choice to test their knowledge with different number of questions.
* To provide users with the option to open the leader board and view and compare the top ranking 3 players, for the number of questions they selected.

## User Stories
* As a user I want to play a fun game about one of my favourite movies.
* As a user I want to be able to select the number of questions I can play.
* As a user I want to be able to view and compare the scores of the top 3 ranking players.

# The Scope Plane
## Features planned:
* As there are certain restrictions in the scope of the development for the application, such as the terminal confines and methods of deployment. It will be important to ensure all functionality is contained within the game terminal screen.
* Despite the confines of the terminal window, the site should be visually stimulating with a graphic/image behind it and clear to the user that it is a quiz.
* Question amount options should be available to the user, 10, 15, and 20 giving the game a sense of longevity. 

# The Structure Plane
User Story: 
> As a user, I want a fun and simple quiz to test my knowledge.

Acceptance Criteria:

* It should be clear to the user that this is a quiz, what the quiz is about, and how to play with the option to pick how many questions asked.

Implementation:

* The layout, as this is a terminal-based game, the use of colour within the game and a background image will be designed to immerse the user into the film trivia quiz. Implementing a sense of fun throughout the interactions of the game. The welcome message at the start of the game will give the user clear instructions on what they are playing and how to play, with clear prompts to the user and validation for each user input.

User story: 
> As a user, I want to be able to check my score and to see where I rank in a leader board. 

Acceptance Criteria:

* The user should have the option to check a leader board to see where they placed in the top three, depending on the number of questions asked.
* The users score will be captured in a separate spread sheet, along with their name and if they are lucky enough to score within the top three they will have their name and score displayed to the terminal with their ranking position.

# Logical flow
I used lucid charts to help me visualise the projects functionality throughout the development process. This helped me a great deal in planning the logic behind the game and how each input the user put in would be checked. 

![Game_flow](/assets/images/game_flow.png)
![Game_flow_two](/assets/images/game_flow_two.png)

# The Skeleton Plane
## Wireframe mock-ups
As the application will be run within a terminal emulator which was provided within the CI template, there are limited options available regarding how the programme is displayed. The theme of the quiz came from my own passion of the movie's. To make it more of an appealing UI experience and more visually stimulating for the user, I located a suitable background image on peakpx.com. I changed the position of the terminal and the button to the centre of the screen with the user experience in mind, also I changed the colour of the button and gave it a background shadow to match the background image, giving it a more incorporated look and feel, to the terminal.

## Game Loop
The player will either pick to start the game or view the leader board by entering 1 or 2, after the player inputs 1 the player will be asked for their name, then the user will be asked to select the number of questions they wish to play. Each functionality checks for correct user input and passes relative data to each function.

# The Surface Plane 
## Design
After creating my quiz, I found a suitable image from the Back to the Future movie and felt it fitted perfectly with the theme of the quiz.

## Class C
I added a class to hold colour variables to implement into my project, I got the idea from a helpful member of the slack community who guided me to this website so 
I could implement colour into my Python project. I used the green colour to indicate a correct answer, I used red to indicate an incorrect answer and yellow to display the points gained within the game. I also used the colours on my leader board for better visual effect. In the run.py there is a warning for the Class "C" which states "Class name "C" doesn't conform to Pascal Case naming style". I wanted to keep the variable name small as my leader board was getting errors for the line being too long and for easer readability. 

![Colour class c](/assets/images/color_c_class.png)

[Link](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html)

# Features
## Welcome Screen
At the start of the game the user is greeted with a message, welcoming them to the quiz and asking them what options they would like to do depending on if they want to play the game, or view the leader board. Players have clear instructions of how to proceed with these options.

![Welcome Screen](/assets/images/welcome_message.png)

## Leader board
If the user selects the option 2, it will print to the terminal the top 3 winning names and scores. I have added a colour feature within the scores so that the 1st 2nd and 3rd are easily visible to the player, also the number of points they scored is lit up in blue for better readability. 

![Leader board Screen](/assets/images/leaderboard.png)

## Start Game Screen
Once a player has entered 1, they will be asked to enter their name, this will show an error message if they don't enter alphabetical characters. Once they have entered their name the game will ask how many questions they would like to answer, again if they do not enter numerical digits, they will receive an error message and be asked again. After these initial steps have been taken the game will then start and generate a random set of questions.

![Player Name Input](/assets/images/enter_name.png)

![Round Input](/assets/images/question_amount.png)

![Example Error Screen](/assets/images/enter_quetion_answer_error.png)

# Quiz Questions
I used a separate file, Questions.py, to import from. This contains the 20 quiz questions and all the optional answers, including the correct answer for each question.
Once a question is generated the player will have the option to select from a group of multiple-choice answers, with only one being correct. Once the player has selected their option which is going to be either a) b) or c), the faction then checks and validated the answer to make sure it is correct. The player will then see a visual score which will indicate whether they got a question right as if they did it will add a point to their score, if answered incorrectly they will not gain a point and the next random question will be generated. If the player does not input the correct letter, they will again be presented with an error message and given the option to try again.

![Question Example](/assets/images/question.png)

# Game End
Once the player has answered their selected number of questions, their name and score will be updated to the google spread sheet and if they make the top 3 their data will be displayed in the leader board. The player will now be congratulated with their score and given the option to press 'n' to end the game, if the 'n' option is selected the game thanks the player and indicates how to reset the game. The player is also given the option press 'y' to play again, the player will then be given the option to change the number of questions they would like to play.

![End Game message](/assets/images/end_game_message.png)

![End Game message no selection](/assets/images/end_game_no_selection.png)

![End Game message yes selection](/assets/images/end_game_yes_selection.png)

# Future Enhancements
In the future, I would add more questions to the questions file as although it generates the questions randomly there are currently only 20 questions.

## Testing 
During the testing process of all the different inputs, I check that each input took the user to the correct part of the game and each wrong input displayed the correct error message. I came across a bug after finishing the game. The player is asked if they would like to play again and asked how many questions they would like, if the player had chosen 10 questions for 1st round and then tried to pick any other amount above 10 the game broke and displayed a Value Error message. This is because there was not enough question to satisfy the requirement.

![Game Bug Image](/assets/images/end_game_bug.png)

![Game bug Image Bottom](/assets/images/end_game_bug_bottom.png)

To fix this issue I created another variable inside the "start game" function called "quiz_questions_list" and assigned it quiz_question.copy(). This then generated a copy of the questions used in the game. In an ideal world I would of had more questions but eventually the same issue would of arise, doing it this way I’m reusing questions that have already been asked to satisfy the requirements needed.

## Validator Testing

pep8online.com - I utilized pep8online.com to validate my python code. All the python files were checked with only one error in my questions.py no new line at end of file I added a new line and ran the test again with no other errors.

![Validator Error](/assets/images/code_validator_error.png)

![Validator No Error](/assets/images/code_validated_no_error.png)

![Validator Run.py](/assets/images/validator_run.py.png)

# Libraries Utilised
## Built-in Python Libraries
I used several of the built in Python libraries to enable additional functionality within the application math.

## Time
The time library was also imported to utilize the time. Sleep functionality. This enabled me to incorporate specific time delays within the program which adds to the player experience by simulating the time between the player answering their points going up or their correct/wrong message before the next question is displayed.

## OS
The os library was imported to utilize the os.system and os.name functionality. This enabled me to add functionality to the terminal emulator which allowed me to clear the previous print statements. This provides a clearer and more structured experience for the user.

## Random
The random library was imported to access several the built-in methods of generating a random question.

## GSpread
I also added in the GSpread function which allowed me to link the API for google sheets into the file so I could successfully create a leader board that would change on every player's input.

# Deployment 
The site was deployed via Heroku, and the live link can be found here - [link to page](https://back-to-the-future-quiz.herokuapp.com/)

The project was developed utilising a Code Institute provided template.

## Project Deployment
To deploy the project through Heroku I followed these steps:

Sign up / Log in to [Link to Heroku](https://dashboard.heroku.com/apps)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* * Give the project a name - I entered back-to-the-future-quiz and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the settings tab.
* This next step is required for creating the app when using the CI Python Deployment Template. If you created your own program without using the CI Template, you might not need to add a config var.
* In the config vars section select the reveal config vars button. This will display the current config vars for the app, there should be nothing already there.
* In the KEY input field input PORT all in capitals, then in the VALUE field input 8000 and select the Add button to the right.
Next select the add build pack button below the config vars section.
* In the pop-up window select Python as your first build pack and select save changes.
* Then repeat the steps to add a node.js build pack.
* The order of the build packs is important, in the list Python should be first with Node.js second. If they are not in this order, you can click and drag them to rearrange.
* Next navigate back to the deploy tab using the submenu at the top of the page.
* In the deployment method section select the GitHub - Connect to GitHub button and follow the steps prompted if any to connect your GitHub account
* In the Connect to GitHub section that appears, select the correct account, and enter the name of the repository and select search.
* Once Heroku has located the repo select connect.
* This will connect the repo to the app within Heroku. Below the Apps Connected to Heroku section will be the Automatic Deploys section.
* In this section, confirm the correct branch of the repo is selected in the drop-down box, and then click the Enable Automatic Deploys button
* This will ensure whenever you change something in the repo and push the changes to GitHub, Heroku will rebuild the app. If you prefer to do this manually you can utilise the manual deployment options further down. For this project I utilised the Automatic Deployment to enable me to check changes I made to the app as I developed it.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

# Credits
## Code
I was informed of a method to clear the terminal by another student on the course Matt Bodden who had found the method in a Python cheat sheet provided by [coding4you](http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf).

## Content
### stack Overflow
I used stack overflow to help my understanding of pulling information from a dictionary and various other small functionalities that I needed reminding of.

# Acknowledgement

I would like to thank the following:

* Matt Bodden for always being there to talk through any issues that arise, also helping me with the functions and processes needed for my code to run smoothly.
He is a great support on the slack community group.



