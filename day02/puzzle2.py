import math


def sum_game_power(filename: str) -> int:
    with open(filename, "r") as file:
        total = 0
        for line in file:
            game = line.strip().split(":")[1]
            rounds = game.split("; ")
            n_cubes = {"red": [1], "blue": [1], "green": [1]}
            for r in rounds:
                for cube in r.split(", "):
                    x = cube.split()
                    n_cubes[x[1]].append(int(x[0]))
            total += math.prod(max(quants) for _, quants in n_cubes.items())

    return total


assert sum_game_power("day02/test_input") == 2286
print(sum_game_power("day02/input"))
