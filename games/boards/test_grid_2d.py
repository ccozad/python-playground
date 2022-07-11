from games.boards.grid_2d import Grid2D


def test_constructor():
    grid = Grid2D(4,3, "?")
    assert grid.width == 4
    assert grid.height == 3
    assert len(grid.board) == 12
    assert grid.board[0] == "?"

def test_get_set():
    grid = Grid2D(3,3, "?")
    grid.set_cell(0, 0, "A")
    grid.set_cell(0, 1, "B")
    grid.set_cell(0, 2, "C")
    grid.set_cell(1, 0, "D")
    grid.set_cell(1, 1, "E")
    grid.set_cell(1, 2, "F")
    grid.set_cell(2, 0, "G")
    grid.set_cell(2, 1, "H")
    grid.set_cell(2, 2, "I")

    assert grid.get_cell(0, 0) == "A"
    assert grid.get_cell(0, 1) == "B"
    assert grid.get_cell(0, 2) == "C"
    assert grid.get_cell(1, 0) == "D"
    assert grid.get_cell(1, 1) == "E"
    assert grid.get_cell(1, 2) == "F"
    assert grid.get_cell(2, 0) == "G"
    assert grid.get_cell(2, 1) == "H"
    assert grid.get_cell(2, 2) == "I"