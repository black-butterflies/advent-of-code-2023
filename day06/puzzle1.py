def result(filename: str) -> int:
    with open(filename, "r") as file:
        times = [int(i) for i in file.readline().strip().split()[1:]]
        records = [int(i) for i in file.readline().strip().split()[1:]]

    total = 1
    for i, t in enumerate(times):
        r = records[i]
        if t % 2:
            end = t // 2
            ways = 0
        else:
            end = int(t / 2) - 1
            ways = 1

        for j in range(0, end + 1):
            d = j * (t - j)
            if d > r:
                break

        ways += 2 * ((end + 1) - j)
        total *= ways

    return total


assert result("day06/test_input") == 288
print(result("day06/input"))
