"""
This is problem to convert all the negative coordinates to a positive coordinates;
The agenda is to get all the coordinates in 0 or positive values keeping the relative distance same;
We can add or delete any number from the coordinates ; however graph should not be changed;

Input: [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
Output : [(9,6), (6, 12), (7,7),(0, 5), (8, 12), (18,5)]
"""

def convert_to_positive_coordinates(coordinates):
    min_x = min(x for x, y in coordinates)
    min_y = min(y for x, y in coordinates)
    
    shift_x = -min_x if min_x < 0 else 0
    shift_y = -min_y if min_y < 0 else 0
    
    return [(x + shift_x, y + shift_y) for x, y in coordinates]

input_coordinates = [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
output_coordinates = convert_to_positive_coordinates(input_coordinates)
print(output_coordinates)
