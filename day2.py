
class Submarine():
    def __init__(self):
        self.horizontal_position = 0
        self.depth = 0
        self.aim = 0

    def move_part1(self, instruction: str):
        direction, units = instruction.split(' ')
        units = int(units)
        if direction == 'forward':
            self.horizontal_position += units
        elif direction == 'down':
            self.depth += units
        else:
            # direction == 'up'
            self.depth -= units

    def move_part2(self, instruction: str):
        direction, units = instruction.split(' ')
        units = int(units)
        if direction == 'forward':
            self.horizontal_position += units
            self.depth += self.aim * units
        elif direction == 'down':
            self.aim += units
        else:
            # direction == 'up'
            self.aim -= units


def get_input():
    with open('inputs/day2.txt', 'r') as f:
        instructions = [elt.strip() for elt in f.readlines()]
    return instructions


def part1():
    instructions = get_input()
    s = Submarine()
    for instruction in instructions:
        s.move_part1(instruction)
    return s.horizontal_position * s.depth


def part2():
    instructions = get_input()
    s = Submarine()
    for instruction in instructions:
        s.move_part2(instruction)
    return s.horizontal_position * s.depth


if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part2()
    print(f"Part 2 answer is {answer2}")
