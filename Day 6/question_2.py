def read_file(filename: str) -> list:
    file_input = []
    with open(filename) as file:
        for line in file:
            input_list = list(map(int, line.rstrip().split(',')))
            file_input.append(input_list)
    return file_input[0]


if __name__ == '__main__':
    fish_states = read_file('input.txt')

    day = 1

    day_count_map = {x: 0 for x in range(-1, 9)}

    for x in fish_states:
        day_count_map[x] += 1

    while day < 257:
        for i in range(0, 9):
            day_count_map[i-1] = day_count_map[i]
        day_count_map[8] = day_count_map[-1]
        day_count_map[6] += day_count_map[-1]
        day_count_map[-1] = 0
        day += 1

    print(sum(day_count_map.values()))
