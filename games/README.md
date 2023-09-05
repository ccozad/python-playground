# Introduction

Python is a general purpose language that allows one to easily model the game state of common game types

# Topics

 - Boards
   - [2D grid](/games/boards/grid_2d.py) A simple representation of a 2D grid board that can be used for games like tic-tac-toe or checkers
   - [Tic-tac-toe board](/games/boards/tic_tac_toe_board.py) A board based on a 2D Grid that is specialized for the rules of tic-tac-toe
 - Cards
   - [Card deck](/games/cards/card_deck.py) A collection of cards that can be shuffled and dealt
   - [Card deck factory](/games/cards/card_deck_factory.py) A simplified way to construct various types of card decks
   - [Playing card](/games/cards/playing_card.py) A representation of a standard playing card
 - Clients
   - [Tic-tac-toe client](/games/game_clients/tic_tac_toe_client.py) Play tic-tac-toe using a simple command line client
 - Other
   - [Runiks Cube Simulator](/games/rubiks_cube/rubiks-cube-2x2.py) Simulate moves on a 2x2 Rubik's cube

# Rubik's Cube Simulator

Run the simulator using an input file with a list of moves.

```
% cd gmaes/rubiks_cube
% python3 rubiks-cube-2x2.py --input moves-1.txt 

Start
G G
G G

U
R R
G G

R
R Y
G Y

R
R B
G O

D
R B
O O

D
R B
R B

L
W B
W B

U
R R
W B

U
G W
W B

End
```

# Game Client Usage

Game clients are interactive programs that allow you to change the game world state. Running each game client is usually just a matter of running a particular Python file but additional details are provided below.

# Tic-tac-toe Client

Run the client with the command `./games/game_clients/tic_tac_toe_client.py` This will start an interactive CLI client to make plays and view the board. The commands available include:

```
Commands: 
play m,n        Current player makes a play at position m,n
board           Shows the current state of the board
restart         Restart the game
help            Print list of commands
exit            Exit the game
```

The desired command is entered at the prompt. The play action will use the symbol for the current turn.

```
Current turn: O
Command:`
```

Positions are given as `row,column`. The board uses the following numbers for rows and columns:

```
Command: board
   0   1   2
0  ? | ? | ?
  ---+---+---
1  ? | ? | ?
  ---+---+---
2  ? | ? | ?
```

**[Back to start](https://github.com/ccozad/python-playground)**