
class Entry:
    def __init__(self, unique_patterns, output):
        self.unique_patterns = unique_patterns
        self.output = output


def read_file(filename: str) -> list:
    file_input = []
    with open(filename) as file:
        for line in file:
            input_list = list(line.rstrip().split(' | '))
            unique_signal_patterns = input_list[0].split(' ')
            four_digit_output = input_list[1].split(' ')
            file_input.append(Entry(unique_signal_patterns, four_digit_output))
    return file_input


if __name__ == '__main__':
    entries = read_file('input.txt')
    unique_entry_map = {
        # Number of Unique: Digit
        2: '1',
        4: '4',
        3: '7',
        7: '8',
    }

    digit_counter = 0
    for entry in entries:
        for digit in entry.output:
            if len(digit) in unique_entry_map:
                digit_counter += 1

    print(digit_counter)
