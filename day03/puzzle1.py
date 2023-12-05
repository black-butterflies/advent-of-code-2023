def part_number_check(lines: list[str], line_idx: int, number_idxs: list[int]) -> int:
    # want the list of lines, the index of the line we're looking at
    # and the idxs of the number we're checking
    max_idx = len(lines[line_idx]) - 1
    extended_idxs = []
    if number_idxs[0] > 0:
        extended_idxs = [(number_idxs[0] - 1, line_idx)]
    extended_idxs.extend((n, line_idx) for n in number_idxs)
    if number_idxs[-1] < max_idx:
        extended_idxs.append((number_idxs[-1] + 1, line_idx))

    if line_idx > 0:
        prev_idxs = [(char_idx, l_idx - 1) for char_idx, l_idx in extended_idxs]
    else:
        prev_idxs = []

    if line_idx < len(lines) - 1:
        next_idxs = [(char_idx, l_idx + 1) for char_idx, l_idx in extended_idxs]
    else:
        next_idxs = []

    # remove the original numbers
    extended_idxs = [
        (char_idx, l_idx)
        for char_idx, l_idx in extended_idxs
        if char_idx not in number_idxs
    ]

    all_idxs = prev_idxs + extended_idxs + next_idxs
    is_part_number = False
    for char_idx, l_idx in all_idxs:
        char = lines[l_idx][char_idx]
        if not char.isdigit() and char != ".":
            is_part_number = True

    if is_part_number:
        return int(lines[line_idx][number_idxs[0] : number_idxs[-1] + 1])
    else:
        return 0


def sum_part_numbers(filename: str) -> int:
    with open(filename, "r") as file:
        lines = [line.strip() for line in file]

    number_idxs = {}
    for j, line in enumerate(lines):
        is_prev_digit = False
        for i, char in enumerate(line):
            is_digit = char.isdigit()
            if not is_prev_digit and is_digit:
                if j not in number_idxs:
                    number_idxs[j] = [[i]]
                else:
                    number_idxs[j].append([i])
            elif is_prev_digit and is_digit:
                number_idxs[j][-1].append(i)
            is_prev_digit = is_digit

    total = 0
    for line_idx, nums in number_idxs.items():
        for idxs in nums:
            total += part_number_check(lines, line_idx, idxs)

    return total


assert sum_part_numbers("day03/test_input") == 4361
print(sum_part_numbers("day03/input"))
