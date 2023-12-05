stages = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


def get_minimum_location(filename: str) -> int:
    with open(filename, "r") as file:
        seeds = [int(s) for s in file.readline().strip().split(": ")[1].split()]
        file.readline()

        full_map = {}
        for _ in range(len(stages)):
            name = file.readline().split()[0]
            current_maps = []
            line = file.readline().strip()
            while line != "":
                current_maps.append(tuple(int(val) for val in line.strip().split()))
                line = file.readline().strip()
            full_map[name] = current_maps

    locations = []

    for seed in seeds:
        start = seed
        for stage in stages:
            stage_maps = full_map[stage]
            available_map = False
            for destination, source, length in stage_maps:
                if start in range(source, source + length):
                    available_map = True
                    break
            if available_map:
                diff = start - source
                start = destination + diff
        locations.append(start)

    return min(locations)


assert get_minimum_location("day05/test_input") == 35
print(get_minimum_location("day05/input"))
