import os
from math import prod

input_path = os.path.join(os.path.dirname(__file__), 'input')
with open(input_path) as input_list:
    formatted_list = [line.strip() for line in input_list]


(rows, cols) = (len(formatted_list), len(formatted_list[0]))


def count_trees(right, down):
    stops = [ formatted_list[step*down][(step*right)%cols]
              for step in range(0,((rows-1)//down)+1)]
    return len([ stop for stop in stops if stop == '#' ])


slopes = [(3,1), (1,1), (5,1), (7,1), (1,2)]

print(f"Part 1: {count_trees(*slopes[0])}")
print(f"Part 2: {prod([count_trees(r,d) for r,d in slopes])}")


