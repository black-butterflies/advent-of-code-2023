def total_points(filename: str) -> int:
    total = 0
    with open(filename, "r") as file:
        for line in file:
            numbers = line.strip().split(": ")[1].split(" | ")
            winning = set(int(n) for n in numbers[0].split())
            yours = set(int(n) for n in numbers[1].split())

            matches = len(winning & yours)
            if matches > 0:
                total += 2 ** (matches - 1)

    return total


assert total_points("day04/test_input") == 13
print(total_points("day04/input"))
