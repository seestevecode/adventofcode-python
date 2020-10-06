import os

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input_path) as input_file:
    original_polymer = input_file.read().splitlines()[0]

"""
Heavily influenced by r/adventofcode solution
"""

LOW_A = ord("a")
UPP_A = ord("A")


def react(polymer):
    old_polymer = None
    while old_polymer != polymer:
        old_polymer = polymer
        for i in range(26):
            polymer = polymer.replace(chr(LOW_A + i) + chr(UPP_A + i), "")
            polymer = polymer.replace(chr(UPP_A + i) + chr(LOW_A + i), "")
    return len(polymer)


print("Part 1:", react(original_polymer))

test_counts = {}
for i in range(26):
    polymer = original_polymer.replace(
        chr(LOW_A + i), "").replace(chr(UPP_A + i), "")
    test_counts[chr(LOW_A + i)] = react(polymer)
else:
    print("Part 2:", min(test_counts.values()))
