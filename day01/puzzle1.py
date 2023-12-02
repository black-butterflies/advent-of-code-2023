def calibration(filename: str) -> int:
    total = 0
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            for i in range(len(line)):
                if line[i].isdigit():
                    left = line[i]
                    break
            for j in range(len(line) - 1, -1, -1):
                if line[j].isdigit():
                    right = line[j]
                    break

            total += int(left + right)

    return total


assert calibration("day01/puzzle1_test_input") == 142

print(calibration("day01/input"))
