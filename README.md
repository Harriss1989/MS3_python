# Back to the Future Quiz (MS3_python)
## Introduction
Back to the Future Quiz (MS3_python) is a browser-based game built in Python. It is a fun quiz game focusing on the Back To The Future movie franchise, and also my favourite movie of all time.

This game utilises the Code Institute Python template, as it was developed in Python for use in the terminal. This makes it available within a web browser.

![Game image]()

[Link to live site](https://back-to-the-future-quiz.herokuapp.com/) If you would like to open this document in a new browser tab, please press CTRL + Click.

# UX
## The Strategy Plane
* Back To The Future quiz game is designed to be a fun quiz for fans of the Back To The Future movie, players can challenge themselves on their triva knowledge from the movie and test themselves on what they can remember. Player scores will be recorded in a spreadsheet and the top 3 will be displayed in the terminal. There is the option to choose the amount of questions played, either 10, 15 or 20 depending on how challenging the player would like the quiz to be.

## Site Goals
* To provide users and die-hard fans of the movie, with an fun and simple to play quiz.
* To provide users and die-hard fans of the movie, the choice to test there knowledge with different amount of questions.
* To provide users with the option to open the leaderboard and view and compare the top ranking 3 players, for the amount of questions they selected.

## User Stories
* As a user I want to play a fun game about one of my favourite movies.
* As a user I want to be able to select the number of questions I can play.
* As a user I want to be able to view and compare the scores of the top 3 ranking players.

# The Scope Plane
## Features planned:
* As there are certain resrictions in the scope of the development fof the application, such as the termimal confines and methods of deployment. It will be important to ensure all functionality is contained within the game terminal screen.
* Dispite the confines of the terminal window, the site should be visually stimulating with a graphic/image behind it and clear to the user that it is a quiz.
* Question amount options should be avalible to the user, 10, 15, and 20 giving the game a sense of longevity. 

# The Structure Plane
User Story: 
> As a user, I want a fun and simple quiz to test my knowledge.

Acceptance Criteria:

* It should be clear to the user that this is a quiz, what the quiz is about, and how to play with the option to pick how many questions asked.

Implementation:

* The layout, as this is a terminal based game, the use of colour within the game and a background image will be designed to immerse the user into the film triva quiz. Implementing a sense of fun through out the interactions of the game. The welcome message at the start of the game will give the user clear instrutions on what they are playing and how to play, with clear prompts to the user and validation for each user input.

User story: 
> As a user, I want to be able to check my score and to see where I rank in a leaderboard. 

Acceptance Criteria:

* The user should have the option to check a leaderboard to see where they placed in the top three, depending on the amount of questions asked.
* The users score will be captured in a seperate spread sheet, along with their name and if they are lucky enough to score within the top three they will have there name and score desplayed to the terminal with their ranking position.

# Logical flow
I used lucid charts to help me visualise the projects functionallity through out the development process. This helped me a great deal in planning the logic behind the game and how each input the user put in would be checked. 

![Game_flow]()
![Inputted_data]()

# The Skeleton Plane
## Wireframe mock-ups
As the application will be run within a terminal emulator which was provided within the CI template, there are limited options available in regards to how the programe is displayed. The theme of the quiz came from my own passion of the movie's. To make it more of an appealing UI experience and more visualy stimulating for the user, I located a suitable background image on peakpx.com. I changed the position of the terminal and the button to the center of the screen with the user experiance in mind, also I changed the colour of the button and gave it a background shadow to match the background image, giving it a more incorparated look and feel, to the termianl.

## Game Loop
The player will either pick to start the game or view the leaderboard by entering 1 or 2, after the player inputs 1 the player will be asked for there name, then the user will be asked to select the amount of questions they wish to play. Each funtionality checks for correct user input and passes relative data to each function.

# The Surface Plane 
## Design
After creating my quiz I found a suitable image from the Back to the Future movie and felt it fitted perfectly with the theme of the quiz.

## Class C
I added a class to hold colour varibles to implement into my project, I got the idea from a helpful member of the slack community who guided me to this website so 
I could implemet colour into my Python project. I used the green colour to indicate a correct answer, I used red to indicate an incorrect answer and yellow to display the points gained within the game. I also used the colours on my leaderboard for better visual effect.

![Link](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html)

# Features
## Welcome Screen
At the start of the game the user is greeted with a message, welcoming them to the quiz and asking them what options they would like to do depending on if they want to play the game, or view the leaderboard. Players have clear instructions of how to proceed with these options.

![Welcome Screen]()

## Leaderboard
If the user selects the option 2, it will print to the terminal the top 3 winning names and scores. I have added a colour feature within the scores so that the 1st 2nd and 3rd are easily visable to the player, also the amount of points they scored is lit up in blue for better readability. 

![Leaderboard Screen]()

## Start Game Screen
Once a player has entered 1 they will be asked to enter their name, this will show an error message if they don't enter alphabetical characters. Once they have entered their name the game will ask how many questions they would like to answer, again if they do not enter numerical digits they will recieve an error message and be asked again. After these inital steps have been taken the game will then start and generate a random set of questions.

![Player Name Input]()
![Round Input]()
![Example Error Screen]()

# Quiz Questions
I used a seperate file, Questions.py, to import from. This contains the 20 quiz questions and all the optional answers, including the correct answer for each question.
Once a question is generated the player will have the option to select from a group of multiple choice answers, with only one being correct. Once the player has seleted their option which is going to be either a) b) or c), the fuction then checks and validated the answer to make sure it is correct. The player will then see a visual score which will indicate whether they got a question right as if they did it will add a point to their score, if answered incorrectly they will not gain a point and the next random question will be generated.

![Question Example]()