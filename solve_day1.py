import day1

with open ('day1.txt') as f:
    data = f.read()

print('Day One Part One Answer:')
print(day1.part_one(data))

print('Day One Part Two Answer:')
print(day1.part_two(data))