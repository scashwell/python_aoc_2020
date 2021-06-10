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

target = 2020

def test_day_one_part_one():
    assert day1.part_one(data) == 514579

def test_strings_to_int():
    assert day1.strings_to_int(data) == integers

def test_find_two_sum():
    assert day1.find_two_sum(integers, target) == (299, 1721)

def test_day_one_part_two():
    assert day1.part_two(data) == 241861950

def test_find_three_sum():
    assert day1.find_three_sum(integers, target) == {979, 366, 675}