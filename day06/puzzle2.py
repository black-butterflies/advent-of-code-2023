def result(filename: str) -> int:
    with open(filename, "r") as file:
        t = int("".join(file.readline().strip().split()[1:]))
        r = int("".join(file.readline().strip().split()[1:]))

    total = 1
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


assert result("day06/test_input") == 71503
print(result("day06/input"))
