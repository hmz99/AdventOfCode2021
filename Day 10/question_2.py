def read_file(filename: str) -> list:
    file_input = []
    with open(filename) as file:
        for line in file:
            file_input.append(list(line.rstrip()))
    return file_input



if __name__ == '__main__':
    chunk_lines = read_file('input.txt')
    score_map = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    chunk_map = {
        '[': ']',
        '{': '}',
        '(': ')',
        '<': '>'
    }
    chunk_openers = list(chunk_map)

    scores = []
    incomplete_lines = []
    for line in chunk_lines:
        tracking_stack = []
        is_complete = False
        for indicator in line:
            if indicator in chunk_openers:
                tracking_stack.append(indicator)
            else:
                if tracking_stack:
                    expected_closer = chunk_map[tracking_stack.pop()]
                    if indicator != expected_closer:
                        is_complete = True
                else:
                    is_complete = True
        if not is_complete:
            incomplete_lines.append(line)
    

    for line in incomplete_lines:
        tracking_stack = []
        line_score = 0
        for indicator in line:
            if indicator in chunk_openers:
                tracking_stack.append(indicator)
            else:
                if tracking_stack:
                    # Since it's valid this should work
                    tracking_stack.pop()
        if tracking_stack:
            # closed in reverse
            for elem in tracking_stack[::-1]:
                expected_closer = chunk_map[elem]
                line_score = (line_score * 5) + score_map[expected_closer]
        
        scores.append(line_score)

    scores = sorted(scores)
    middle_elem = len(scores) // 2
    print(scores[middle_elem])