with open("day_10/input.txt", "r+") as f:
    input_list = f.read().splitlines()

dictionary_of_symbols = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

dictionary_of_points_per_symbol_pair = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

subtotal = 0

for line in input_list:

    list_of_opened_chars = []
    for char in line:
        if char in dictionary_of_symbols.keys():  # Openings
            list_of_opened_chars.append(char)
        else:
            if char == dictionary_of_symbols[list_of_opened_chars[-1]]:  # Closings
                # Check if closing matches LAST opening
                list_of_opened_chars.pop(-1)
            else:
                subtotal += dictionary_of_points_per_symbol_pair[char]
                break

print(subtotal)
# Find and discard corrupted lines first
# ???
