
class LanternfishSchool():
    def __init__(self, initial_timers):
        self.timers = {
            idx: len([elt for elt in initial_timers if elt == idx])
            for idx in range(9)
        }

    def update(self):
        new_timers = {idx: 0 for idx in range(9)}
        for timer, value in self.timers.items():
            if timer > 0:
                new_timers[timer - 1] += value
            else:
                new_timers[6] += value
                new_timers[8] += value
        self.timers = new_timers


def get_input():
    with open('inputs/day6.txt') as f:
        line = f.readline().strip()
    return [int(elt) for elt in line.split(',')]


def run(n):
    initial_timers = get_input()
    fishes = LanternfishSchool(initial_timers)
    for _ in range(n):
        fishes.update()
    return sum(fishes.timers.values())


if __name__ == "__main__":
    answer1 = run(80)
    print(f"Part 1 answer is {answer1}")
    answer2 = run(256)
    print(f"Part 2 answer is {answer2}")
