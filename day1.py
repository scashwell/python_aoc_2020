def part_one(data):
    expenses = strings_to_int(data)
    first, second = find_two_sum(expenses, 2020)
    return first * second

def strings_to_int(data):
    return list(map(int, data.split()))

def find_two_sum(integers, target_sum):
    # for i in integers:
    #     for j in integers:
    #         if i + j == 2020:
    #             return {i, j}
    integers.sort()
    low_index = 0
    high_index = -1
    total = 0
    count = 0
    while total != target_sum:
        count +=1
        total = integers[low_index] + integers[high_index]
        if total == target_sum:
            return (integers[low_index], integers[high_index])
        elif low_index == len(integers)-1 or high_index == 0-len(integers):
            break
        elif total > target_sum:
            high_index -= 1
        elif total < target_sum:
            high_index = -1
            low_index += 1
        
def part_two(data):
    expenses = strings_to_int(data)
    first, second, third = find_three_sum(expenses, 2020)
    return first * second * third

def find_three_sum(integers, target_sum):
    for i in integers:
        new_integers = integers
        new_integers.remove(i)
        new_target_sum = target_sum - i
        result = find_two_sum(new_integers, new_target_sum)
        if result is None:
            continue
        else:
            return {i, result[0], result[1]}
