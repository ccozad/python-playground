from games.boards.tic_tac_toe_board import TicTacToeBoard

def test_constructor():
    tttb = TicTacToeBoard()
    assert tttb.width == 3
    assert tttb.height == 3
    assert "".join(tttb.board) == "?????????"

def test_make_move():
    tttb = TicTacToeBoard()
    tttb.make_move("O", 0, 0)
    tttb.make_move("X", 1, 0)
    tttb.make_move("O", 0, 1)
    tttb.make_move("X", 2, 0)
    tttb.make_move("O", 0, 2)

    assert "".join(tttb.board) == "OOOX??X??"

def test_winner_row_0():
    tttb = TicTacToeBoard()
    tttb.board[0] = "O"
    tttb.board[1] = "O"
    tttb.board[2] = "O"
    tttb.board[3] = "X"
    tttb.board[6] = "X"

    assert tttb.winner() == "O"

def test_winner_row_1():
    tttb = TicTacToeBoard()
    tttb.board[3] = "O"
    tttb.board[4] = "O"
    tttb.board[5] = "O"
    tttb.board[0] = "X"
    tttb.board[6] = "X"

    assert tttb.winner() == "O"

def test_winner_row_2():
    tttb = TicTacToeBoard()
    tttb.board[6] = "O"
    tttb.board[7] = "O"
    tttb.board[8] = "O"
    tttb.board[0] = "X"
    tttb.board[3] = "X"

    assert tttb.winner() == "O"

def test_winner_col_0():
    tttb = TicTacToeBoard()
    tttb.board[0] = "O"
    tttb.board[3] = "O"
    tttb.board[6] = "O"
    tttb.board[1] = "X"
    tttb.board[7] = "X"

    assert tttb.winner() == "O"

def test_winner_col_1():
    tttb = TicTacToeBoard()
    tttb.board[1] = "O"
    tttb.board[4] = "O"
    tttb.board[7] = "O"
    tttb.board[0] = "X"
    tttb.board[6] = "X"

    assert tttb.winner() == "O"

def test_winner_col_2():
    tttb = TicTacToeBoard()
    tttb.board[2] = "O"
    tttb.board[5] = "O"
    tttb.board[8] = "O"
    tttb.board[0] = "X"
    tttb.board[6] = "X"

    assert tttb.winner() == "O"

def test_winner_diag_0():
    tttb = TicTacToeBoard()
    tttb.board[0] = "O"
    tttb.board[4] = "O"
    tttb.board[8] = "O"
    tttb.board[1] = "X"
    tttb.board[6] = "X"

    assert tttb.winner() == "O"

def test_winner_diag_1():
    tttb = TicTacToeBoard()
    tttb.board[2] = "O"
    tttb.board[4] = "O"
    tttb.board[6] = "O"
    tttb.board[1] = "X"
    tttb.board[0] = "X"

    assert tttb.winner() == "O"

def test_no_winner():
    tttb = TicTacToeBoard()
    tttb.board[2] = "O"
    tttb.board[4] = "O"
    tttb.board[1] = "X"
    tttb.board[0] = "X"

    assert tttb.winner() == None
