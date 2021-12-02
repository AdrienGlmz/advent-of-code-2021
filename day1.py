
def get_input():
    with open('inputs/day1.txt', 'r') as f:
        depths = [int(elt.strip()) for elt in f.readlines()]
    return depths


def count_num_of_increases(x, y):
    return sum([a < b for a, b in zip(x, y)])


def part1():
    depths = get_input()
    return count_num_of_increases(depths, depths[1:])


def part2():
    depths = get_input()
    return count_num_of_increases(depths, depths[3:])


if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part2()
    print(f"Part 2 answer is {answer2}")
