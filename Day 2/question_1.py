def read_file(filename: str) -> list:
    file_input = []
    with open(filename) as file:
        for line in file:
            vals = line.rstrip().split(' ')
            file_input.append([vals[0], int(vals[1])])
    return file_input


def calculate_horizontal(vals: list) -> int:
    hor_distance = 0
    for path in vals:
        direction = path[0]
        units = path[1]
        if direction == 'forward':
            hor_distance += units
    return hor_distance


def calculate_vertical(vals: list) -> int:
    ver_distance = 0
    for path in vals:
        direction = path[0]
        units = path[1]
        if direction == 'down':
            ver_distance += units
        elif direction == 'up':
            ver_distance -= units
    return ver_distance


if __name__ == '__main__':
    values = read_file('input.txt')

    hor_dis = calculate_horizontal(values)
    ver_dis = calculate_vertical(values)

    print(hor_dis * ver_dis)
