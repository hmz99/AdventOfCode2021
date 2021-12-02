def read_file(filename: str) -> list:
    file_input = []
    with open(filename) as file:
        for line in file:
            vals = line.rstrip().split(' ')
            file_input.append([vals[0], int(vals[1])])
    return file_input


def calculate_distance(vals):
    aim = 0
    vertical_dist = 0
    horizontal_dist = 0
    for x in vals:
        if x[0] == 'up':
            aim -= x[1]

        if x[0] == 'down':
            aim += x[1]

        if x[0] == 'forward':
            horizontal_dist += x[1]
            vertical_dist += aim * x[1]

    return vertical_dist * horizontal_dist


if __name__ == '__main__':
    values = read_file('input.txt')

    print(calculate_distance(values))