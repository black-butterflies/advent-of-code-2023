def calibration_spell(filename: str) -> int:
    total = 0
    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            found = False
            for i in range(len(line)):
                if found:
                    break
                if line[i].isdigit():
                    left = line[i]
                    found = True
                    break
                for d in digits:
                    if line[i:].startswith(d):
                        left = digits[d]
                        found = True
                        break

            found = False
            for j in range(len(line) - 1, -1, -1):
                if found:
                    break
                if line[j].isdigit():
                    right = line[j]
                    found = True
                    break
                for d in digits:
                    if line[: j + 1].endswith(d):
                        right = digits[d]
                        found = True
                        break

            total += int(left + right)
    return total


assert calibration_spell("day01/puzzle2_test_input") == 281
print(calibration_spell("day01/input"))
