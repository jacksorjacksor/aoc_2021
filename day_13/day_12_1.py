input = ["start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"]

list_of_caves = []


class Cave:
    def __init__(self, name):
        self.name = name
        self.big = self.name.isupper()
        self.connections = []

    def __repr__(self) -> str:
        return self.name


def cave_check(point1, point2):
    is_it_new = True
    for cave in list_of_caves:
        if cave.name == point1:
            is_it_new = False
            new_cave = cave
    if is_it_new:
        new_cave = Cave(point1)
    if point2 not in new_cave.connections:
        new_cave.connections.append(point2)
    if is_it_new:
        list_of_caves.append(new_cave)


for item in input:
    point1, point2 = item.split("-")
    cave_check(point1, point2)
    cave_check(point2, point1)

# Check every possible route which:
## Has to start and end at the start and end
## Has to visit all capitals
## Can only visit small rooms once


print(list_of_caves)

route_list = []

current_location = [cave for cave in list_of_caves if cave.name == "start"][0]

for cave in current_location.connections:
    