
def get_inputs():
    with open('inputs/day12.txt', 'r') as f:
        lines = [elt.strip() for elt in f.readlines()]
    return lines


def get_adjacent_graph_representation(edges):
    output_dict = dict()
    for e in edges:
        start, end = e.split('-')
        if output_dict.get(start):
            output_dict[start].append(end)
        else:
            output_dict[start] = [end]
        if output_dict.get(end):
            output_dict[end].append(start)
        else:
            output_dict[end] = [start]
    return output_dict


def get_all_valid_path(start, adjacents, twice):
    def count_paths(current_node, seen, twice):
        if current_node.islower():
            seen = seen.union({current_node})
        nb_paths = 0

        for node in adjacents[current_node]:
            if node == 'end':
                nb_paths += 1
            elif node not in seen:
                nb_paths += count_paths(node, seen, twice)
            elif node != 'start' and twice:
                nb_paths += count_paths(node, seen, False)
        return nb_paths
    return count_paths(start, frozenset(), twice)


def part1():
    edges = get_inputs()
    adjacent_nodes = get_adjacent_graph_representation(edges)
    return get_all_valid_path('start', adjacent_nodes, False)

def part2():
    edges = get_inputs()
    adjacent_nodes = get_adjacent_graph_representation(edges)
    return get_all_valid_path('start', adjacent_nodes, True)


if __name__ == "__main__":
    answer1 = part1()
    print(f"Part1 answer is {answer1}")
    answer2 = part2()
    print(f"Part2 answer is {answer2}")
