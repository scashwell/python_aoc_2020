import day1
data = '''
    1721
    979
    366
    299
    675
    1456
    '''

integers = [1721, 979, 366, 299, 675, 1456]

def test_day_one_part_one():
    assert day1.part_one(data) == 514579

def test_strings_to_int():
    assert day1.strings_to_int(data) == integers

def test_find_two_sum():
    assert day1.find_two_sum(integers, 2020) == (1721, 299)