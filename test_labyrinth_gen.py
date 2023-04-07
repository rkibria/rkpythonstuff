from labyrinth_gen import make_labyrinth

def test_single_cell():
    labyrinth = make_labyrinth(1, 1, 0)
    assert(labyrinth["size"] == (1,1))
    assert(labyrinth["cells"] == [[[True, True, True, True]]]) # Walls: NSWE, True=closed

def test_two_columns_by_one_row():
    labyrinth = make_labyrinth(1, 2, 0)
    assert(labyrinth["size"] == (1, 2))
    # open east wall <-> open west wall
    assert(labyrinth["cells"] == [[[True, True, True, False], [True, True, False, True]]])

def test_one_column_by_two_rows():
    labyrinth = make_labyrinth(2, 1, 0)
    assert(labyrinth["size"] == (2, 1))
    # open south wall
    # |
    # open north wall
    assert(labyrinth["cells"] == [[[True, False, True, True]], [[False, True, True, True]]])
