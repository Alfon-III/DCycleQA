def inc(x):
    return x + 1


# pytest '.\Exercise 1.py'
def test_answer():
    assert inc(4) == 5
    # assert inc(3) == 5
    # assert inc(5) == 6
    # assert inc(3) == 3
