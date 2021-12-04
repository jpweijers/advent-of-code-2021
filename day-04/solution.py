import re
with open('input.txt') as input_file:
    content = input_file.read().split("\n\n")

    numbers = [int(n) for n in content[0].split(',')]
    boards = []
    for c in content[1:]:
        board = re.split(r'\s+', c.strip())
        board = [int(x) for x in board]
        board = [board[x:x+5] for x in range(0, len(board), 5)]
        boards.append(board)

    row_cols = [boards[i] + [list(x) for x in list(zip(*boards[i]))]
                for i in range(len(boards))]


def play(last):
    lst = []
    won = []
    cur = (0, 0)

    for n in numbers:
        lst.append(n)
        for player in row_cols:
            for row_col in player:
                if all(x in lst for x in row_col):
                    unmarked_sum = sum(set([
                        x for y in player for x in y if x not in lst]))
                    if not last:
                        return lst[~0]*unmarked_sum
                    cur = (unmarked_sum, lst[~0]) if row_cols.index(
                        player) not in won else cur
                    won.append(row_cols.index(player))
    return cur[0]*cur[1]


answer_one = str(play(False))
answer_two = str(play(True))
print("p1: " + answer_one)
print("p2: " + answer_two)
