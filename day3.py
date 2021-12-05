
def get_input():
    with open('inputs/day3.txt', 'r') as f:
        binary_codes = [list(elt.strip()) for elt in f.readlines()]
    return binary_codes


def count_by_digit(binary_codes, digit):
    count = {'0': 0, '1': 0}
    for code in binary_codes:
        count[code[digit]] += 1
    return count


def filter_by_digit(binary_codes, filter, digit):
    return [code for code in binary_codes if code[digit] == filter]


def part1():
    binary_codes = get_input()
    counts = [count_by_digit(binary_codes, d) for d in
              range(0, len(binary_codes[0]))]
    gamma, epsilon = [], []
    for digit in counts:
        digit_sorted = sorted(digit.items(), key=lambda x: x[1])
        gamma.append(digit_sorted[-1][0])
        epsilon.append(digit_sorted[0][0])
    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)


def part2():
    oxygen, co2 = get_input(), get_input()
    max_digit = len(oxygen[0])
    for d in range(max_digit):
        if len(oxygen) > 1:
            count_oxygen = count_by_digit(oxygen, d)
            most_common = sorted(count_oxygen.items(),
                                 key=lambda x: x[1])[-1][0]
            oxygen = filter_by_digit(oxygen, most_common, d)
        if len(co2) > 1:
            count_co2 = count_by_digit(co2, d)
            least_common = sorted(count_co2.items(), key=lambda x: x[1])[0][0]
            co2 = filter_by_digit(co2, least_common, d)
    return int(''.join(oxygen[0]), 2) * int(''.join(co2[0]), 2)


if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part2()
    print(f"Part 2 answer is {answer2}")
