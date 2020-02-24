from copy import deepcopy


def solution(map):
    shortest = len(map) * len(map[0])
    changes = [(0, 0)]

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 1:
                empty = 0

                for xstep, ystep in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    empty += 1 if 0 <= x + xstep < len(map[y]) and 0 <= y + ystep < len(map) and map[y + ystep][x + xstep] == 0 else 0

                changes.append((x, y)) if empty > 1 else None

    for xchange, ychange in changes:
        changed = deepcopy(map)
        changed[ychange][xchange] = 0
        steps = 1
        paths, stepped = [(0, 0)], [(0, 0)]

        while (len(changed[0]) - 1, len(changed) - 1) not in stepped and steps < shortest:
            add, remove = [], []

            for xpath, ypath in paths:
                for xstep, ystep in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    if (xpath + xstep, ypath + ystep) not in stepped and 0 <= xpath + xstep < len(changed[0]) and 0 <= ypath + ystep < len(changed) and changed[ypath + ystep][xpath + xstep] == 0:
                        stepped.append((xpath + xstep, ypath + ystep))
                        add.append((xpath + xstep, ypath + ystep))

                remove.append((xpath, ypath))

            paths = [path for path in paths if path not in remove] + add
            steps += 1

        shortest = steps

    return shortest


if __name__ == '__main__':
    print('pass' if solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) == 7 else 'fail')
    print('pass' if solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 11 else 'fail')
