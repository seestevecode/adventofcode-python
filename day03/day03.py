# Input
input_list = open('input.txt')
formatted_list = [line.rstrip() for line in input_list]


def create_shape(string):
    """ Create shape from row string as ID and set of coords """

    shape_id = int(string.split('#')[1].split('@')[0])

    top_left_x = int(string.split(' @ ')[1].split(',')[0])
    top_left_y = int(string.split(' @ ')[1].split(',')[1].split(':')[0])

    width = int(string.split(':')[1].split('x')[0])
    height = int(string.split('x')[1])

    xs = range(top_left_x, top_left_x + width)
    ys = range(top_left_y, top_left_y + height)

    shape = shape_id, {(x, y) for x in xs for y in ys}
    return shape


# Create set of all shapes and list of all shape ID
shapes = {}
shape_ids = []
for row in formatted_list:
    shape_id, shape_coords = create_shape(row)
    shapes[shape_id] = shape_coords
    shape_ids.append(shape_id)

overlaps = set()  # Create set to store overlaps between pairs

# Loop through distinct pairs of shapes
for shape1_id, shape1_coords in shapes.items():
    for shape2_id, shape2_coords in shapes.items():
        if shape2_id > shape1_id:
            # If shapes overlap, remove ID from list
            # and add intersection to overlaps set
            if shape1_coords.intersection(shape2_coords):
                if shape1_id in shape_ids:
                    shape_ids.remove(shape1_id)
                if shape2_id in shape_ids:
                    shape_ids.remove(shape2_id)
                overlaps.update(shape1_coords.intersection(shape2_coords))
else:
    print("Part 1:", len(overlaps))  # Size of overlaps set
    print("Part 2:", shape_ids[0])  # Remaining ID with no overlaps
