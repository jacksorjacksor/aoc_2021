with open("day_09/input.txt", "r+") as f:
    file_contents = f.read().splitlines()

list_of_low_points = []
number_of_rows = len(file_contents)
number_of_cols = len(file_contents[0])


def existance_checker(row, col):
    if row < 0 or col < 0 or row > number_of_rows or col > number_of_cols:
        return 10
    try:
        return int(file_contents[row][col])
    except:
        return 10


for index_of_row, value_of_row in enumerate(file_contents):
    for index_of_col, value_of_col in enumerate(value_of_row):
        # Go through all orthog points: TLBR
        top_point = existance_checker(index_of_row - 1, index_of_col)
        right_point = existance_checker(index_of_row, index_of_col + 1)
        bottom_point = existance_checker(index_of_row + 1, index_of_col)
        left_point = existance_checker(index_of_row, index_of_col - 1)

        list_of_adjacent_points = [top_point, right_point, bottom_point, left_point]

        is_low_point = True

        for comparison in list_of_adjacent_points:
            if comparison <= int(value_of_col):
                is_low_point = False
        if is_low_point:
            list_of_low_points.append(int(value_of_col))

print(sum([item + 1 for item in list_of_low_points]))
