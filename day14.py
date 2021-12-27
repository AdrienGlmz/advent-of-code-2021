
class Polymer():
    def __init__(self, initial_chain, rules):
        pairs = [initial_chain[idx:(idx+2)]
                 for idx in range(len(list(initial_chain)) - 1)]
        chain = {p: 0 for p in set(rules.keys())}
        for p in pairs:
            chain[p] += 1
        self.chain = chain
        self.rules = rules
        self.last_element = initial_chain[-1]

    def get_pairs(self):
        return

    def add_step(self):
        new_pairs = {p: 0 for p in set(self.rules.keys())}
        for p, nb in self.chain.items():
            if self.rules.get(p):
                two_pairs = p[0] + self.rules[p] + p[1]
                pair1, pair2 = two_pairs[:2], two_pairs[1:]
                new_pairs[pair1] += nb
                new_pairs[pair2] += nb
            else:
                new_pairs[p] = nb
        self.chain = new_pairs

    def get_nb_elements(self):
        all_elements = set(list(''.join(self.rules.keys())))
        elements = {elt: 0 for elt in all_elements}
        for p, nb in self.chain.items():
            elt1, elt2 = p[0], p[1]
            elements[elt1] += nb
        elements[self.last_element] += 1
        return elements.items()

def get_inputs():
    with open('inputs/day14.txt', 'r') as f:
        lines = f.readlines()
    chain = lines.pop(0).strip()
    rules = dict()
    for elt in lines[1:]:
        pair, new_elt = elt.strip().split(' -> ')
        rules[pair] = new_elt
    return chain, rules

def main(k):
    chain, rules = get_inputs()
    p = Polymer(chain, rules)
    for i in range(k):
        p.add_step()
    nb_elements = sorted(p.get_nb_elements(), key=lambda x: x[1])
    return nb_elements[-1][1] - nb_elements[0][1]


if __name__ == "__main__":
    answer1 = main(10)
    print(f"Part 1 answer is {answer1}")
    answer2 = main(40)
    print(f"Part 2 answer is {answer2}")
