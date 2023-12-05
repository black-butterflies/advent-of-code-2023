def total_points(filename: str) -> int:
    cards = []
    with open(filename, "r") as file:
        for line in file:
            numbers = line.strip().split(": ")[1].split(" | ")
            winning = set(int(n) for n in numbers[0].split())
            yours = set(int(n) for n in numbers[1].split())

            matches = len(winning & yours)
            cards.append([matches, 1])

    for i, (m, q) in enumerate(cards):
        for _ in range(q):
            for j in range(m):
                cards[i + j + 1][1] += 1

    return sum(quant for _, quant in cards)


assert total_points("day04/test_input") == 30
print(total_points("day04/input"))
