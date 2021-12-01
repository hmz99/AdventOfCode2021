def read_file(filename: str) -> list:
    file_input = []
    with open(filename) as file:
        for line in file:
            file_input.append(int(line.rstrip()))
    return file_input


def count_increases(values: list) -> int:
    increase_counter = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            increase_counter += 1

    return increase_counter


if __name__ == '__main__':
    values = read_file('input.txt')

    increases = count_increases(values)

    print(increases)
