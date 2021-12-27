import numpy as np

def get_inputs():
    with open('inputs/day15.txt', 'r') as f:
        lines = [elt.strip() for elt in f.readlines()]
    lines = [list(map(int, list(elt))) for elt in lines]
    return lines

def get_full_map():
    raw_inputs = np.array(get_inputs())
    full_cave_map = np.array(get_inputs())

    for row in range(1, 5):
        new_values = (raw_inputs + row - 1) % 9 + 1
        full_cave_map = np.append(full_cave_map, new_values, axis=0)

    raw_inputs = full_cave_map.copy()
    for column in range(1, 5):
        new_values = (raw_inputs + column - 1) % 9 + 1
        full_cave_map = np.append(full_cave_map, new_values, axis=1)

    return full_cave_map


def shortest_path_dijkstra(start_node, risk_map):
    m = np.array(risk_map)
    n_rows, n_cols = m.shape

    visited = set()
    distances = np.full_like(m, 1e5)
    # Initialize with the starting node
    to_visit = {start_node}
    distances[start_node] = 0

    i = 0

    while to_visit:
        weighted_dict = {node: distances[node] for node in list(to_visit)}
        l = sorted(weighted_dict.items(),
                      key=lambda x: x[1], reverse=False)
        (x, y), _ = l[0]
        to_visit.remove((x, y))

        choices = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        neighbors = [
            (x, y) for x, y in choices
            if (0 <= x < n_rows) and (0 <= y < n_cols)
        ]
        for node in neighbors:
            if node not in visited:
                if distances[node] > (distances[(x, y)] + m[node]):
                        distances[node] = (distances[(x, y)] + m[node])
                if node not in to_visit:
                    to_visit.add(node)
        visited.add((x, y))
    return distances[(n_rows - 1, n_cols - 1)]


if __name__ == "__main__":
    lines = get_inputs()
    answer1 = shortest_path_dijkstra((0, 0), lines)
    print(f"Part 1 answer is {answer1}")
    full_map = get_full_map()
    answer2 = shortest_path_dijkstra((0, 0), full_map)
    print(f"Part 2 answer is {answer2}")
