import os
input_path = os.path.join(os.path.dirname(__file__), 'input')
with open(input_path) as input_list:
    formatted_list = [int(line) for line in input_list]

part_one = [i for i in formatted_list if 2020 - i in formatted_list]
part1 = part_one[0] * part_one[1]

for i in formatted_list:
    part_two = [j for j in formatted_list if 2020 - i - j in formatted_list]
    if part_two != []:
        part2 = i * part_two[0] * part_two[1]
        break
