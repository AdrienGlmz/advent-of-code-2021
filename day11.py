import numpy as np

class Octopuses:
    def __init__(self, initial_energy_level):
        self.energy_level = np.pad(initial_energy_level,
                                   1, constant_values=-1e15)
        self.flashes = 0
        self.simultaneous_flash = 0
        self.step = 0

    def add_step(self):
        self.energy_level += 1
        flashed_idx = set()
        idx_x, idx_y = np.where(self.energy_level > 9)
        to_process = set(zip(list(idx_x), list(idx_y))) - flashed_idx
        while to_process:
            # idx_x and idx_y have same shape
            for x, y in to_process:
                adjacents_idx = [(x-1, y-1), (x-1, y), (x-1, y+1),
                                 (x, y-1), (x, y+1),
                                 (x+1, y-1), (x+1, y), (x+1, y+1)]
                for i, j in adjacents_idx:
                    self.energy_level[i, j] += 1
                flashed_idx.add((x, y))
                idx_x, idx_y = np.where(self.energy_level > 9)
                to_process = set(zip(list(idx_x), list(idx_y))) - flashed_idx
        for x, y in flashed_idx:
            self.energy_level[x, y] = 0
        self.step += 1
        self.flashes += len(list(flashed_idx))
        if len(list(flashed_idx)) == (self.energy_level.shape[1] - 2) * (self.energy_level.shape[0] - 2):
            self.simultaneous_flash += 1

def get_inputs():
    with open('inputs/day11.txt', 'r') as f:
        lines = [elt.strip() for elt in f.readlines()]
        lines = [[int(e) for e in elt] for elt in lines]
    return lines

def part1():
    inputs = get_inputs()
    oct = Octopuses(inputs)
    for _ in range(100):
        oct.add_step()
    return oct.flashes


def part2():
    inputs = get_inputs()
    oct = Octopuses(inputs)
    while not oct.simultaneous_flash:
        oct.add_step()
    return oct.step

if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part2()
    print(f"Part 2 answer is {answer2}")
