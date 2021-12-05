
class HydrothermalVents():
    def __init__(self, vents):
        self.vents = vents
        self.vents_expanded = dict()
        self.coverage = dict()

    def expand(self, include_diag=False):
        for v in self.vents:
            beginning, end = v.split(' -> ')
            x_start, y_start = map(lambda x: int(x), beginning.split(','))
            x_end, y_end = map(lambda x: int(x), end.split(','))
            # Reorder
            x_min, x_max = min(x_start, x_end), max(x_start, x_end)
            y_min, y_max = min(y_start, y_end), max(y_start, y_end)
            if x_start == x_end:
                # horizontal line
                self.vents_expanded[v] = (
                    [(x_start, y) for y in range(y_min, y_max + 1)]
                )
            elif y_start == y_end:
                # vertical line
                self.vents_expanded[v] = (
                    [(x, y_start) for x in range(x_min, x_max + 1)]
                )
            else:
                # diagonal line at 45 degrees
                if include_diag:
                    x_range = (
                        range(x_min, x_max + 1)[::(2*(x_start < x_end) - 1)]
                    )
                    y_range = (
                        range(y_min, y_max + 1)[::(2*(y_start < y_end) - 1)]
                    )
                    self.vents_expanded[v] = (
                        [(x, y) for x, y in zip(x_range, y_range)]
                    )

    def compute_coverage(self):
        for v, points in self.vents_expanded.items():
            for p in points:
                if self.coverage.get(p):
                    self.coverage[p] += 1
                else:
                    self.coverage[p] = 1
        return self.coverage


def get_inputs():
    with open('inputs/day5.txt', 'r') as f:
        lines = [elt.strip() for elt in f.readlines()]
    return lines


def part1(include_diag=False):
    lines = get_inputs()
    hv = HydrothermalVents(lines)
    hv.expand(include_diag=include_diag)
    coverage = hv.compute_coverage()
    return sum([elt >= 2 for elt in coverage.values()])

if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part1(include_diag=1)
    print(f"Part 2 answer is {answer2}")
