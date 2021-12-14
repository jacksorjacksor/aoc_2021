with open("day_10/input.txt", "r+") as f:
    input_list = f.read().splitlines()

dictionary_of_symbols = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

dictionary_of_points_per_symbol_pair = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

list_of_subtotals = []
for line in input_list:
    good_list = True
    subtotal = 0
    list_of_opened_chars = []
    for char in line:
        if char in dictionary_of_symbols.keys():  # Openings
            list_of_opened_chars.append(char)
        else:
            if char == dictionary_of_symbols[list_of_opened_chars[-1]]:  # Closings
                # Check if closing matches LAST opening
                list_of_opened_chars.pop(-1)
            else:
                good_list = False
                break
    if good_list:
        print(line)
        list_of_opened_chars.reverse()
        print(list_of_opened_chars)
        for char in list_of_opened_chars:
            subtotal *= 5
            subtotal += dictionary_of_points_per_symbol_pair[
                dictionary_of_symbols[char]
            ]

        list_of_subtotals.append(subtotal)

list_of_subtotals.sort()

for sub in list_of_subtotals:
    print(sub)


print(list_of_subtotals)

print(list_of_subtotals[int(len(list_of_subtotals) / 2)])
