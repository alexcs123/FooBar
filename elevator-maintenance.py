from operator import itemgetter


def solution(l):
    j = []

    for version in l:
        broken = (version + '.0.0.0').split('.')

        for part in range(len(broken)):
            broken[part] = int(broken[part])

        j.append(broken)

    for version in j:
        version[3] = len(version)

    c = sorted(j, key=itemgetter(0, 1, 2, 3))

    for u, h in enumerate(c):
        x = ''
        for z in range(len(h) - 3):
            x += '.' + str(h[z])
        c[u] = x[1:]

    return c


if __name__ == '__main__':
    print('pass' if solution(['1.11', '2.0.0', '1.2', '2', '0.1', '1.2.1', '1.1.1', '2.0']) == ['0.1', '1.1.1', '1.2', '1.2.1', '1.11', '2', '2.0', '2.0.0'] else 'fail')
    print('pass' if solution(['1.1.2', '1.0', '1.3.3', '1.0.12', '1.0.2']) == ['1.0', '1.0.2', '1.0.12', '1.1.2', '1.3.3'] else 'fail')
