from math import lcm


def count_steps(filename: str) -> int:
    network = {}
    starting_nodes = []
    with open(filename, "r") as file:
        path = file.readline().strip()
        file.readline()
        for line in file:
            x = line.strip().split(" = ")
            if x[0].endswith("A"):
                starting_nodes.append(x[0])
            network[x[0]] = tuple(x[1][1:-1].split(", "))

    node_counts = []
    for node in starting_nodes:
        next_step = node
        i = 0
        steps = 0
        while not next_step.endswith("Z"):
            op = path[i]
            next_step = network[next_step][0 if op == "L" else 1]
            steps += 1
            i = (i + 1) % len(path)
        node_counts.append(steps)

    return lcm(*node_counts)


assert count_steps("day08/test3_input") == 6
print(count_steps("day08/input"))
