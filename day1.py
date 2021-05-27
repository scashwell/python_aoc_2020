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
        if total > target_sum:
            high_index -= 1
        elif total < target_sum:
            high_index = -1
            low_index += 1
        else:
            return (integers[low_index], integers[high_index])

