class Board:
    
    def __init__(self, board, board_item_map, total) -> None:
        self.board = board
        self.board_item_map = board_item_map
        self.total = total

    def contains(self, value):
        return value in self.board_item_map

    def mark_value(self, value):
        if not self.contains(value):
            return False
        else:
            for i in range(0, len(self.board)):
                for j in range(0, len(self.board[i])):
                    if self.board[i][j] == value:
                        self.board[i][j] = 'x'
                        self.total -= int(value)
        return True

    def check_victory(self):
        
        for i in range(0, len(self.board)):
            row = []
            column = []
            for j in range(0, len(self.board[i])):
                row.append(self.board[i][j])
                column.append(self.board[j][i])

            if len(set(row)) == 1:
                if 'x' in set(row):
                    return True
            
            if len(set(column)) == 1:
                if 'x' in set(column):
                    return True

        return False


def read_file(filename: str) -> list:
    with open(filename) as file:
        input_lines = []
        for line in file:
            input_lines.append(line.rstrip())

    winning_numbers = input_lines[0].split(',')
    boards = []
    board = []
    board_items = []
    for line in input_lines[2:]:
        line = line.split(' ')
        line = [value for value in line if value != '']
        if line:
            board_items += line
            board.append(line)
        else:
            total = sum(list(map(int, board_items)))
            board_items = set(board_items)
            boards.append(Board(board, board_items, total))
            board = []
            board_items = []
    total = sum(list(map(int, board_items)))
    board_items = set(board_items)
    boards.append(Board(board, board_items, total))
    return winning_numbers, boards




if __name__ == '__main__':
    winning_numbers, boards = read_file('input.txt')
    
    last_number = 0
    last_board = 0
    board_tracker = {i:boards[i] for i in range(0, len(boards))}
    winning_scores = []
    for number in winning_numbers:
        for i in range(0, len(boards)):
            if i in board_tracker:
                board_tracker[i].mark_value(number)
                if board_tracker[i].check_victory():
                    score = board_tracker[i].total * int(number)
                    winning_scores.append(score)
                    del board_tracker[i]

    print(winning_scores[-1])