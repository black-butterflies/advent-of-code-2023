def count_steps(filename: str) -> int:
    network = {}
    with open(filename, "r") as file:
        path = file.readline().strip()
        file.readline()
        for line in file:
            x = line.strip().split(" = ")
            network[x[0]] = tuple(x[1][1:-1].split(", "))

    next_step = "AAA"
    i = 0
    steps = 0
    while next_step != "ZZZ":
        op = path[i]
        next_step = network[next_step][0 if op == "L" else 1]
        steps += 1
        i = (i + 1) % len(path)

    return steps


assert count_steps("day08/test_input") == 2
assert count_steps("day08/test2_input") == 6
print(count_steps("day08/input"))
