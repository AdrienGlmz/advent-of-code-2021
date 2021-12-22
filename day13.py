import numpy as np
import matplotlib.pyplot as plt

class TransparentPaper():
    def __init__(self, initial_positions):
        self.positions = initial_positions

    def fold(self, instruction):
        new_positions = []
        axis, line = instruction.split('=')
        line = int(line)
        if axis == 'fold along y':
            # Fold bottom half up
            max_y = max([elt[1] for elt in self.positions])
            for pos in self.positions:
                curr_x, curr_y = pos
                if curr_y > line:
                    curr_y = (max_y - curr_y)
                new_positions.append((curr_x, curr_y))
        else:
            # Fold left
            max_x = max([elt[0] for elt in self.positions])
            for pos in self.positions:
                curr_x, curr_y = pos
                if curr_x > line:
                    curr_x = (max_x - curr_x)
                new_positions.append((curr_x, curr_y))
        self.positions = list(set(new_positions))

    def print(self):
        max_x = max([int(elt[0]) for elt in self.positions]) + 1
        max_y = max([int(elt[1]) for elt in self.positions]) + 1
        m = np.zeros((max_x, max_y))
        for x, y in self.positions:
            m[x, y] = 1
        plt.imshow(m)
        plt.show()


def get_inputs():
    with open('inputs/day13.txt', 'r') as f:
        lines = f.readlines()
    idx = lines.index('\n')
    dots, instructions = lines[:idx], lines[(idx+1):]
    dots = [tuple(map(int, elt.split(','))) for elt in dots]
    instructions = [elt.strip() for elt in instructions]
    return dots, instructions


def part1():
    dots, instructions = get_inputs()
    paper = TransparentPaper(dots)
    paper.fold(instructions[0])
    return len(paper.positions)

def part2():
    dots, instructions = get_inputs()
    paper = TransparentPaper(dots)
    for instruction in instructions:
        print(instruction)
        paper.fold(instruction)
    paper.print()


if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    part2()
