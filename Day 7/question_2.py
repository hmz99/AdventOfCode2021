from collections import defaultdict

def step_cost(n):
    cost = 0
    for i in range(1, n+1):
        cost += i
    return cost


def read_file(filename: str) -> list:
    file_input = []
    with open(filename) as file:
        for line in file:
            input_list = list(map(int, line.rstrip().split(',')))
            file_input.append(input_list)
    return file_input[0]


if __name__ == '__main__':
    initial_positions = read_file('input.txt')
    initial_positions = sorted(initial_positions)
    initial_position_map = defaultdict(lambda: 0)

    fuel_map = defaultdict(lambda: 0)

    for x in initial_positions:
        initial_position_map[x] += 1

    for x in range(0, initial_positions[-1]):
        for j in set(initial_positions):
            fuel_map[x] += step_cost(abs(x-j)) * initial_position_map[j]

    min_index = min(fuel_map, key=fuel_map.get)
    print(fuel_map[min_index])

