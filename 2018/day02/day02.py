# Input
import os
input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(input_path) as input_list:
    formatted_list = [line.rstrip() for line in input_list]


def count_chars(string):
    chars = list(string)
    counts = []
    for char in set(chars):
        filtered_chars = [c for c in chars if c == char]
        counts.append(len(filtered_chars))
    return (2 in counts, 3 in counts)


def compare_strings(string1, string2):
    if len(string1) != len(string2):
        return None
    diff_idxs = []
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            diff_idxs.append(i)
    if len(diff_idxs) == 1:
        target = diff_idxs[0]
        return string1[:target] + string1[target+1:]
    else:
        return None


# Part 1
count_twos = 0
count_threes = 0
for box_id in formatted_list:
    (has_two, has_three) = count_chars(box_id)
    count_twos += has_two
    count_threes += has_three
else:
    print("Part 1:", count_twos * count_threes)

# Part 2
pairs = [(a, b) for a in formatted_list for b in formatted_list if a != b]
for (string1, string2) in pairs:
    comp = compare_strings(string1, string2)
    if comp != None:
        print("Part 2:", comp)
        break
