def read_file(filename: str) -> list:
    file_input = []
    with open(filename) as file:
        for line in file:
            input_list = list(map(int,line.rstrip()))
            file_input.append(input_list)
    return file_input


if __name__ == '__main__':
    values = read_file('input.txt')

    oxy_input = values.copy()
    bit_position = 0
    while(len(oxy_input) != 1):
        # Transpose
        transposed_list = list(map(list, zip(*oxy_input)))
        most_common_bit_at_position = max(sorted(transposed_list[bit_position], reverse=True), key=transposed_list[bit_position].count)
        oxy_input = [values for values in oxy_input if values[bit_position] == most_common_bit_at_position]
        bit_position += 1

    co2_input = values.copy()
    bit_position = 0
    while(len(co2_input) != 1):
        # Transpose
        transposed_list = list(map(list, zip(*co2_input)))
        most_common_bit_at_position = min(sorted(transposed_list[bit_position]), key=transposed_list[bit_position].count)
        co2_input = [values for values in co2_input if values[bit_position] == most_common_bit_at_position]
        bit_position += 1

    oxy_input_str = "".join(map(str, oxy_input[0]))
    co2_input_str = "".join(map(str, co2_input[0]))

    life_support = int(oxy_input_str, 2) * int(co2_input_str, 2)
    print(life_support)