with open("day_10/input.txt", "r+") as f:
    input_list = f.read().splitlines()

dictionary_of_symbols = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

dictionary_of_points_per_symbol_pair = {
    "(": 3,
    "[": 57,
    "{": 1197,
    "<": 25137,
}

for line in input_list:
    dict_of_results = {}
    points = 0
    for key, item in dictionary_of_symbols.items():
        dict_of_results[key] = len([i for i in line if i == key])
        dict_of_results[item] = len([i for i in line if i == item])
        if dict_of_results[key] == dict_of_results[item]:
            points += dictionary_of_points_per_symbol_pair[key] * dict_of_results[key]
            print(points)
        else:
            break

    # print(dict_of_results)
