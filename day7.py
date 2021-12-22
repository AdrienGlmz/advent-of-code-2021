
def get_inputs():
    with open('inputs/day7.txt', 'r') as f:
        line = f.readline()
    return [int(elt) for elt in line.strip().split(',')]


def cost_part1(initial_positions, target):
    return sum([abs(pos - target) for pos in initial_positions])


def cost_part2(initial_positions, target):
    return sum([
        int((abs(pos - target) * (abs(pos - target) + 1)) / 2)
        for pos in initial_positions
    ])


def run(cost_function):
    initial_positions = get_inputs()
    m, M = min(initial_positions), max(initial_positions)
    costs = []
    for t in range(m, M+1):
        costs.append((t, cost_function(initial_positions, t)))
    return sorted(costs, key=lambda x: x[1])[0]


if __name__ == "__main__":
    answer1 = run(cost_part1)
    print(f"Part 1 answer is {answer1}")
    answer2 = run(cost_part2)
    print(f"Part 2 answer is {answer2}")
