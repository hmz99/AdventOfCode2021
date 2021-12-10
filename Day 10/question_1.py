def read_file(filename: str) -> list:
    file_input = []
    with open(filename) as file:
        for line in file:
            file_input.append(list(line.rstrip()))
    return file_input



if __name__ == '__main__':
    chunk_lines = read_file('input.txt')
    score_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    chunk_map = {
        '[': ']',
        '{': '}',
        '(': ')',
        '<': '>'
    }
    chunk_openers = list(chunk_map)

    scores = []
    for line in chunk_lines:
        tracking_stack = []
        for indicator in line:
            if indicator in chunk_openers:
                tracking_stack.append(indicator)
            else:
                if tracking_stack:
                    expected_closer = chunk_map[tracking_stack.pop()]
                    if indicator != expected_closer:
                        scores.append(score_map[indicator])
                        break
                else:
                    scores.append(score_map[indicator])
                    break

    print(sum(scores))