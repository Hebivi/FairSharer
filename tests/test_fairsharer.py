from fairsharer.fairsharer import fair_sharer


# Test to see if the function gives the right values, tested with 1 and 2 iteration(s)
def test_fair_sharer():
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]
    assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90]
