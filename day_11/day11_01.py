with open("day_11/input.txt", "r+") as f:
    input_list = f.read().splitlines()


class DumboOctopus:
    def __init__(self, row, col, energy_level) -> None:
        self.row = row
        self.col = col
        self.energy_level = energy_level
        self.has_flashed_this_step = False

    def __repr__(self) -> str:
        return f"{self.row},{self.col} || {self.energy_level} || {self.has_flashed_this_step}"


# Make a list of octopus
list_of_dumbo_octopus = []

for row_index, row in enumerate(input_list):
    for col_index, value in enumerate(row):
        list_of_dumbo_octopus.append(DumboOctopus(row_index, col_index, int(value)))

turn_counter = 0
flash_counter = 0

# A node is adjacent if abs(flash_row - node_row) < 2 and abs(flash_col - node_col) < 2 and not node_has_flashed_this_step


while turn_counter < 100:
    turn_counter += 1
    print(f"Turn: {turn_counter}")
    # First, the energy level of each octopus increases by 1.
    for octopus in list_of_dumbo_octopus:
        octopus.energy_level += 1

    # Checks if all flashes are done
    all_flashes_are_done = False
    # Loops until all flashes are done
    while not all_flashes_are_done:

        all_flashes_are_done = True
        for parent_octopus in list_of_dumbo_octopus:
            # Then, any octopus with an energy level greater than 9 *flashes*.
            if (
                parent_octopus.energy_level > 9
                and not parent_octopus.has_flashed_this_step
            ):
                all_flashes_are_done = False
                parent_octopus.has_flashed_this_step = True

                # impact on all adjacacent octopus
                for child_octopus in list_of_dumbo_octopus:
                    if (
                        abs(parent_octopus.row - child_octopus.row) < 2
                        and abs(parent_octopus.col - child_octopus.col) < 2
                        and not child_octopus.has_flashed_this_step
                    ):
                        child_octopus.energy_level += 1

    for octopus in list_of_dumbo_octopus:
        if octopus.has_flashed_this_step:
            flash_counter += 1
            octopus.has_flashed_this_step = False
            octopus.energy_level = 0

    print(f"{turn_counter} | {flash_counter}")
