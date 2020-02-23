from copy import deepcopy


def solution(map):
    shortest = len(map) * len(map[0])
    changes = [(0, 0)]

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 1:
                empty = 0

                for step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    empty += 1 if 0 <= x + step[0] < len(map[y]) and 0 <= y + step[1] < len(map) and map[y + step[1]][x + step[0]] == 0 else 0

                changes.append((x, y)) if empty > 1 else None

    for change in changes:
        changed = deepcopy(map)
        changed[change[1]][change[0]] = 0
        steps = 1
        paths, stepped = [(0, 0)], [(0, 0)]

        while (len(changed[0]) - 1, len(changed) - 1) not in stepped and steps < shortest:
            add, remove = [], []

            for path in paths:
                for step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    if (path[0] + step[0], path[1] + step[1]) not in stepped and 0 <= path[0] + step[0] < len(changed[0]) and 0 <= path[1] + step[1] < len(changed) and changed[path[1] + step[1]][path[0] + step[0]] == 0:
                        stepped.append((path[0] + step[0], path[1] + step[1]))
                        add.append((path[0] + step[0], path[1] + step[1]))

                remove.append(path)

            paths = [path for path in paths if path not in remove] + add
            steps += 1

        shortest = steps

    return shortest


if __name__ == '__main__':
    print('pass' if solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) == 7 else 'fail')
    print('pass' if solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 11 else 'fail')
