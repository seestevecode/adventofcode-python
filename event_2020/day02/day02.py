import os

input_path = os.path.join(os.path.dirname(__file__), 'input')
with open(input_path) as input_list:
    formatted_list = [line.strip() for line in input_list]


# E.g. 17-19 c: ccccccccccfrcctcccjc
def parse_row(row_string):
    [nums, char, string] = row_string.split(' ')
    [fst_num, snd_num] = map(int, nums.split('-'))
    return [fst_num, snd_num, char[0], string]


def check_part1(row_string):
    [min_count, max_count, char, string] = parse_row(row_string)
    char_count = string.count(char)
    return char_count >= min_count and char_count <= max_count


def check_part2(row_string):
    [fst_pos, snd_pos, char, string] = parse_row(row_string)
    return (string[fst_pos - 1] == char) ^ (string[snd_pos - 1] == char)


def count_passed(check_func):
    checked = [check_func(row) for row in formatted_list]
    checked_true = [b for b in checked if b == True]
    return len(checked_true)


print("Part 1: ", count_passed(check_part1))
print("Part 2: ", count_passed(check_part2))
