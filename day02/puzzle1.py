def sum_available_id(filename: str, avail_dict: dict) -> int:
    with open(filename, "r") as file:
        total = 0
        for line in file:
            x = line.strip().split(": ")
            game_id = x[0].split()[1]
            rounds = x[1].split("; ")
            too_many = 0
            for r in rounds:
                cubes = {col.split()[1]: int(col.split()[0]) for col in r.split(", ")}
                too_many += sum(
                    1 for colour, quant in cubes.items() if quant > avail_dict[colour]
                )

            if too_many == 0:
                total += int(game_id)

    return total


avail = {"red": 12, "green": 13, "blue": 14}
assert sum_available_id("day02/test_input", avail) == 8
print(sum_available_id("day02/input", avail))
