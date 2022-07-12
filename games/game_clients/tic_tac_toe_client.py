import sys, os
sys.path.insert(0, os.path.abspath('./'))
from games.boards.tic_tac_toe_board import TicTacToeBoard

done = False
tttb = TicTacToeBoard()
turn = "O"
game_over = False

def play_command(command: str):
    global turn
    positions = command[5:].split(",")
    if len(positions) == 2:
        try:
            row = int(positions[0])
            column = int(positions[1])
            if row >= 0 and row <= 2 and column >= 0 and column <= 2:
                if tttb.is_cell_open(row, column):
                    tttb.make_move(turn, row, column)
                    if turn == "O":
                        turn = "X"
                    else:
                        turn = "O"
                else:
                    print("Position isn't empty!")
            else:
                print("Row and column must be  0, 1 or 2")
        except ValueError as e:
            print(e)
    else:
        print("Invalid play command!")
    

def unknown_command():
    print("Unknown command!")

def board_command():
    print(tttb)

def exit_command():
    global done
    done = True

def restart_command():
    global tttb
    global game_over
    global turn
    tttb = TicTacToeBoard()
    game_over = False
    turn = "O"

def help_command():
    print("Commands: ")
    if not game_over:
        print("play m,n\tCurrent player makes a play at position m,n")
        
    print("board\t\tShows the current state of the board")
    print("restart\t\tRestart the game")
    print("help\t\tPrint list of commands")
    print("exit\t\tExit the game")

def process_command(command: str):
    if command == "help":
        return help_command()
    elif command == "exit":
        return exit_command()
    elif command == "board":
        return board_command()
    elif command == "restart":
        return restart_command()
    elif command.startswith("play") and not game_over:
        return play_command(command)
    else:
        return unknown_command()
    

if __name__ == "__main__":
    print("Let's play tic-tac-toe!")
    help_command()

    while not done:
        print("\nCurrent turn: {}".format(turn))
        command = input("Command: ")
        process_command(command.strip())
        winner = tttb.winner()
        if winner is not None:
            print("{} won the game".format(winner))
            print(":::::::::::::::::::::::::::::::")
            print()
            game_over = True
            help_command()
        
        if tttb.is_cats_game():
            print("The game was a tie")
            print(":::::::::::::::::::::::::::::::")
            print()
            game_over = True
            help_command()
    