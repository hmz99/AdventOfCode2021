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

    while day < 81:

        fish_states = [x-1 for x in fish_states]

        if -1 in fish_states:
            spawn_fish_count = fish_states.count(-1)
            fish_states += [8] * spawn_fish_count

        fish_states = [x if x != -1 else 6 for x in fish_states]

        day += 1

    print(len(fish_states))
