
class Bingo():
    def __init__(self, board):
        self.board = board
        self.dimension = len(board[0])
        self.winner = False
        self.mask = [[0] * len(board[0]) for _ in range(len(board))]

    def check_if_winner(self):
        sum_rows = [sum(l) == self.dimension for l in self.mask]
        sum_cols = [sum(l) == self.dimension for l in zip(*self.mask)]
        self.winner = any(sum_rows) | any(sum_cols)
        return self.winner

    def draw(self, number):
        for b, m in zip(self.board, self.mask):
            if number in b:
                m[b.index(number)] = 1

    def score(self):
        return sum([sum([n for n, b in zip(numbers, bools) if not b])
                    for numbers, bools in zip(self.board, self.mask)])

def get_input():
    with open('inputs/day4.txt', 'r') as f:
        lines = [elt.strip() for elt in f.readlines() if elt != '\n']
        # First row is the random draws
        draws = [int(elt) for elt in lines.pop(0).split(',')]
        # Then each bloc of 5 rows is a single board
        boards = [lines[i:i+5] for i in range(0, len(lines), 5)]
        boards = [[l.split(' ') for l in elt] for elt in boards]
        boards = [[[int(elt) for elt in l if elt != '']
                   for l in board] for board in boards]
    return draws, boards

def part1():
    draws, boards = get_input()
    bingos = [Bingo(b) for b in boards]
    for d in draws:
        [bingo.draw(d) for bingo in bingos]
        winners = [bingo.check_if_winner() for bingo in bingos]
        if sum(winners) >= 1:
            winning_index = winners.index(True)
            return bingos[winning_index].score() * d
    return None


def part2():
    draws, boards = get_input()
    bingos = [Bingo(b) for b in boards]
    winners = []
    for d in draws:
        [bingo.draw(d) for bingo in bingos]
        new_winners = [idx for idx, bingo in enumerate(bingos)
                       if bingo.check_if_winner() and idx not in winners]
        winners.extend(new_winners)
        if len(winners) == len(boards):
            # Stop when every board is a winner
            break
    last_winner_idx = winners[-1]
    return bingos[last_winner_idx].score() * d

if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part2()
    print(f"Part 2 answer is {answer2}")
