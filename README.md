# DIP392-CC4
Harikishore Vasudevan-211ADB011, Allen Joseph Antony-211ADB009

We have chosen to create the game connect-4(four).

Connect 4 is a game that is played by two players on a single screen(grid/board) where the players can drop coins in the empty columns on the board.
Each player will have access to use coins before the start of the game.
The player should be able to make moves (place coin) alternatively by clicking on the desired column on the grid(board).
Each player’s coin has different colours (eg: red for the first player and yellow for the second player).
The first player to connect 4 coins on the grid(board), horizontally, vertically, or diagonally with their assigned colour of the coin, should be declared the winner of the game.
If all the empty holes in the board are filled and none of the players were able to win the game, then it should be declared as a draw.


This game can be liked by those people who wants entertainment and mind-relaxation.
We completed this project using python programming language with libraries pygame, pygame-menu, and numpy.



Link to our Report: https://docs.google.com/document/d/1NafGAOmF-C8TaHY4_WIJ-5H7ONnQ6utDjCWquA6mJjo/edit?usp=sharing

Game coding reference: https://www.askpython.com/python/examples/connect-four-game


Project overview:
A Pygame window will open, displaying the main menu of the game.

Main Menu
The main menu provides the following options:

Play: Starts a new game of Connect 4.
Instructions: Displays the game instructions, explaining the rules and gameplay.
Quit: Exits the game.

Use the mouse to click on the desired option.

Game Screen
When you click on the Play button, a new game screen will appear. The game screen shows the Connect 4 board and provides the following features:

The board consists of a grid of 6 rows and 7 columns.
Players take turns dropping their discs into the columns by clicking on the desired column.
Discs always fall straight down and stack on top of each other.
The game continues until one player successfully connects four discs straight through any direction or the entire board is filled.
If a player wins, a message will be displayed indicating the winning player.
If the game ends in a draw, a message will be displayed indicating a draw.

At the top right corner of the game screen, you will find two buttons:

Back: Clicking on this button will exit the game and return to the main menu.
Restart: Clicking on this button will restart the game, allowing you to play another round, with an empty board.

Instructions Menu:
If you click on the Instructions button from the main menu, an instructions menu will appear. This menu provides a brief overview of the game rules and gameplay.

