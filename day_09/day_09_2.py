with open("day_09/input.txt", "r+") as f:
    file_contents = f.read().splitlines()

list_of_low_points = []

number_of_rows = len(file_contents)
number_of_cols = len(file_contents[0])


class LowPoint:
    def __init__(self, value, row, col, nadir) -> None:
        self.value = value
        self.row = row
        self.col = col
        self.nadir = nadir

    def __repr__(self) -> str:
        return f"{self.value}|({self.row},{self.col})"


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
            list_of_low_points.append(
                LowPoint(int(value_of_col), index_of_row, index_of_col, True)
            )

list_of_basins = []


"""
A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.
"""

# First off - count how many consecutive points afterwards are successively larger than the preceeding one.


def point_finder(row, col):
    if row in range(0, number_of_rows + 1) and col in range(0, number_of_cols + 1):
        return int(file_contents[row][col])
    else:
        return None


# check all points in orthogonal directions

for point in list_of_low_points:
    if point.value == 9:
        continue
    basin = [point]
    row_of_point = point.row
    col_of_point = point.col

    # up:
    while True:
        row_of_point -= 1
        value_of_check = point_finder(row_of_point, col_of_point)
        if not value_of_check or value_of_check <= point_finder(
            row_of_point - 1, col_of_point
        ):
            list_of_basins.append(basin)
            break
        else:
            basin.append(
                LowPoint(int(value_of_check), row_of_point, col_of_point, False)
            )

print(list_of_basins)
# make each point a +
# then see how many are adjacent
# those become SUPER basins
