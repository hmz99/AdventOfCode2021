def read_file(filename: str) -> list:
    file_input = []
    with open(filename) as file:
        for line in file:
            file_input.append(int(line.rstrip()))

    return file_input


def count_increases(values: list) -> int:
    increase_counter = 0
    for i in range(1, len(values)):
        if sum(values[i]) > sum(values[i-1]):
            increase_counter += 1

    return increase_counter


def triplet_slicer(values: list) -> list:
    triple_values = []
    for i in range(0, len(values)-2):
        triple_values.append([values[i], values[i+1], values[i+2]])

    return triple_values


if __name__ == '__main__':
    values = read_file('input.txt')

    triple_values = triplet_slicer(values)

    increases = count_increases(triple_values)
    print(increases)
