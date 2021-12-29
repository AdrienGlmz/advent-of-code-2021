
class Message():
    def __init__(self, binary_rep):
        self.binary_rep = binary_rep
        self.packet_idx = [0]
        self.packet_versions = []
        self.packet_types = []
        self.litteral_packet = []

    def parse_version_and_idx(self, i):
        binary_list = self.binary_rep

        version = binary_list[i:i+3]
        version = int(version, 2)
        self.packet_versions.append(version)
        type = binary_list[i+3:i+6]
        type = int(type, 2)
        self.packet_types.append(type)

        if type == 4:
            # litteral value packet
            end_idx, value = self.parse_litteral_packet(i+6)
        else:
            # operator packet
            end_idx, value = self.parse_operator_packet(i+6, type)
        i = end_idx
        self.packet_idx.append(end_idx)
        return i, value

    def parse_litteral_packet(self, idx):
        dec_nb = []
        while self.binary_rep[idx] != '0':
            dec_nb.append(self.binary_rep[idx+1:idx+5])
            idx += 5
        # Add last digit
        dec_nb.append(self.binary_rep[idx+1:idx+5])
        idx += 5
        value = int(''.join(dec_nb), 2)
        self.litteral_packet.append(value)
        return idx, value

    def parse_operator_packet(self, idx, type):
        length_type_idx = self.binary_rep[idx]
        idx += 1
        values = []

        if length_type_idx == '0':
            total_length = int(self.binary_rep[idx:idx+15], 2)
            idx += 15
            end_idx = idx + total_length
            while idx < end_idx:
                # new packet
                length, value = self.parse_version_and_idx(idx)
                values.append(value)
                idx = length
        else:
            # length_type_idx = 1
            nb_sub_packets = int(self.binary_rep[idx:idx+11], 2)
            idx += 11
            for _ in range(nb_sub_packets):
                length, value = self.parse_version_and_idx(idx)
                values.append(value)
                idx = length
        if type == 0:
            value = sum(values)
        elif type == 1:
            value = 1
            for elt in values:
                value *= elt
        elif type == 2:
            value = min(values)
        elif type == 3:
            value = max(values)
        elif type == 5:
            # only two sub packets
            value = int(values[0] > values[1])
        elif type == 6:
            # only two sub packets
            value = int(values[0] < values[1])
        elif type == 7:
            # only two sub packets
            value = int(values[0] == values[1])
        return idx, value


def get_inputs():
    with open('inputs/day16.txt', 'r') as f:
        line = f.readline().strip()
    binary_representation = []
    for nb in list(line):
        binary_representation.append(f'{int(nb, 16):04b}')
    return ''.join(binary_representation)

def part1():
    b = get_inputs()
    m = Message(b)
    m.parse_version_and_idx(0)
    return sum(m.packet_versions)

def part2():
    b = get_inputs()
    m = Message(b)
    return m.parse_version_and_idx(0)[1]

if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part2()
    print(f"Part 2 answer is {answer2}")
