from subdraw import utils


def test_color():
    assert utils.get_color(10, (1, 2, 3, 4, 5)) == 1


def test_nocolor():
    assert utils.get_color(10, (1, 2, 3, 4, 5), False, 0) == 0
