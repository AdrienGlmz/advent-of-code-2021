
def get_input():
    with open("inputs/day8.txt", 'r') as f:
        lines = [elt.strip().split(' | ') for elt in f.readlines()]
    return lines


class Display():
    def __init__(self, inputs, outputs):
        self.segments =  {
            's1': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
            's2': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
            's3': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
            's4': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
            's5': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
            's6': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
            's7': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        }
        self.digits = {
            '123567': 0,
            '36': 1,
            '13457': 2,
            '13467': 3,
            '2346': 4,
            '12467': 5,
            '124567': 6,
            '136': 7,
            '1234567': 8,
            '123467': 9
        }
        self.inputs = inputs
        self.outputs = outputs

    def decoded(self):
        return all([len(elt) == 1 for elt in self.segments.values()])

    def restrict_segment(self, segment, possibilities):
        # check if this is a feasible configuration
        if not set(possibilities).intersection(set(self.segments[segment])):
            raise Exception('Non feasible configuration')

        # restrict possibilities
        self.segments[segment] = list(set(self.segments[segment]).intersection(set(possibilities)))

    def decode(self):
        info = self.inputs + self.outputs
        info_ordered = {a: [] for a in range(1, 8)}
        # Order available info by length
        for elt in info:
            info_ordered[len(elt)].append(elt)

        # while not self.decoded():
        # Start with elt of len == 2 -> can only be a 1
        for elt in info_ordered[2]:
            # 1 is on s1 or s3 only
            self.restrict_segment('s3', elt)
            self.restrict_segment('s6', elt)

        # len == 3 -> can only be a 7
        for elt in info_ordered[3]:
            self.restrict_segment('s1', elt)
            self.restrict_segment('s3', elt)
            self.restrict_segment('s6', elt)

        # len == 4 -> can only be a 4
        for elt in info_ordered[4]:
            self.restrict_segment('s2', elt)
            self.restrict_segment('s3', elt)
            self.restrict_segment('s4', elt)
            self.restrict_segment('s6', elt)

        # len == 5 -> can be a 2, 3 or 5
        for elt in info_ordered[5]:
            self.restrict_segment('s1', elt)
            self.restrict_segment('s4', elt)
            self.restrict_segment('s7', elt)

        # len == 6 -> can be a 0, 6 or 9
        for elt in info_ordered[6]:
            self.restrict_segment('s1', elt)
            self.restrict_segment('s2', elt)
            self.restrict_segment('s6', elt)
            self.restrict_segment('s7', elt)

        i = 0
        while not self.decoded() and (i < 10):
            i += 1
            sorted_items = sorted(self.segments.items(), key=lambda x: x[1])
            for key, possibilities in sorted_items:
                if len(possibilities) == 1:
                    found_segment = possibilities[0]
                    self.segments = {
                        k: [v for v in value if v != found_segment]
                        for k, value in self.segments.items() if k != key
                    }
                    self.segments[key] = possibilities

        if self.decoded():
            self.reverse_mapping = {
                v[0]: k[1] for k, v in self.segments.items()
            }
            s = []
            for digit in self.outputs:
                decoded_digit = ''.join([
                    self.reverse_mapping[letter] for letter in digit
                ])
                decoded_digit = ''.join(sorted(decoded_digit))
                s.append(str(self.digits.get(decoded_digit)))
            return int(''.join(s))
        else:
            raise Exception("Not able to decode line")


def part1():
    lines = get_input()
    s = 0
    for _, outputs in lines:
        s += len([
            elt for elt in outputs.split(' ') if len(elt) in [2, 3, 4, 7]
        ])
    return s


def part2():
    lines = get_input()
    s = 0
    for inputs, outputs in lines:
        d = Display(inputs.split(" "), outputs.split(" "))
        value = d.decode()
        s += value
    return s


if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part2()
    print(f"Part 2 answer if {answer2}")
