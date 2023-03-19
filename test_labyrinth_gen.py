from labyrinth_gen import make_labyrinth

def test_single_cell():
    labyrinth = make_labyrinth(1, 1, 0)
    assert(labyrinth["size"] == (1,1))
