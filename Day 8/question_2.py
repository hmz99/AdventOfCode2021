
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
    total = 0
    digit_counter = 0
    for entry in entries:
        digits_figured_out = 0
        segment_to_digit_map = {}
        digit_to_segment_map = {}
        unsolved = []
        # Figure out 1,4,7,8
        for x in entry.unique_patterns:
            if len(x) in unique_entry_map:
                digits_figured_out += 1
                segment_to_digit_map[x] = unique_entry_map[len(x)]
                digit_to_segment_map[unique_entry_map[len(x)]] = x
        for x in entry.unique_patterns:
            if len(x) == 6:
                # Possible options are 9,6,0
                if len(set(digit_to_segment_map['1']) - set(x)) == 1:
                    segment_to_digit_map[x] = '6'
                    digit_to_segment_map['6'] = x
                elif len(set(x) - set(digit_to_segment_map['4'])) == 3:
                    segment_to_digit_map[x] = '0'
                    digit_to_segment_map['0'] = x
                else:
                    segment_to_digit_map[x] = '9'
                    digit_to_segment_map['9'] = x
            elif len(x) == 5:
                # Possible options are 2,3,5
                if len(set(x) - set(digit_to_segment_map['1'])) == 3:
                    segment_to_digit_map[x] = '3'
                    digit_to_segment_map['3'] = x

            if x not in segment_to_digit_map:
                unsolved.append(x)  # 2, 5

        for x in unsolved:
            if len(set(x) - set(digit_to_segment_map['6'])) == 0:
                segment_to_digit_map[x] = '5'
            else:
                segment_to_digit_map[x] = '2'

        segment_to_digit_map = {tuple(sorted(x)): value for x, value in segment_to_digit_map.items()}
        output = ""
        for x in entry.output:
            output += segment_to_digit_map[tuple(sorted(x))]
        total += int(output)

    print(total)
