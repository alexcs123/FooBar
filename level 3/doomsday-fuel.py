from numpy import array, identity, transpose
from fractions import Fraction
from math import gcd


def solution(m):
    if len(m) == 1:
        return [1, 1]

    terminals = []

    for i, state in enumerate(m.copy()):
        if state == [0] * (len(m) + len(terminals)):
            del (m[i - len(terminals)])
            terminals.append(i)

    m = list(map(list, zip(*m)))
    deleted = 0

    for i, state in enumerate(m.copy()):
        if i in terminals:
            del (m[i - deleted])
            m.append(state)
            deleted += 1

    m = transpose(array(m).astype('object'))

    for state in m:
        total = sum(state)

        for i, chance in enumerate(state):
            state[i] = Fraction(chance, total)

    a = identity(len(m), Fraction) - m[:, :len(m)]
    b = transpose(m[:, len(m):])
    p = [i for i in range(len(a) + 1)]

    for i in range(len(a)):
        max_a = Fraction(0, 1)
        max_i = i

        for k in range(i, len(a)):
            abs_a = abs(a[k][i])

            if abs_a.numerator * max_a.denominator > max_a.numerator * abs_a.denominator:
                max_a = abs_a
                max_i = k

        if max_a.numerator == 0:
            return b, False

        if not max_i == i:
            j = p[i]
            p[i] = p[max_i]
            p[max_i] = j
            ptr = a[i]
            a[i] = a[max_i]
            a[max_i] = ptr
            p[len(a)] += 1

        for j in range(i + 1, len(a)):
            a[j][i] = a[j][i] / a[i][i]

            for k in range(i + 1, len(a)):
                a[j][k] = a[j][k] - a[j][i] * a[i][k]

    for c in range(len(b)):
        x = [Fraction(0, 1) for i in range(len(a))]

        for i in range(len(a)):
            x[i] = b[c][p[i]]

            for k in range(i):
                x[i] = x[i] - a[i][k] * x[k]

        for i in range(len(a) - 1, -1, -1):
            for k in range(i + 1, len(a)):
                x[i] = x[i] - a[i][k] * x[k]

            x[i] = x[i] / a[i][i]

        b[c] = x

    chances = b[:, 0]
    denominator = chances[0].denominator

    for chance in chances[1:]:
        denominator = int(denominator * chance.denominator / gcd(denominator, chance.denominator))

    chances = [int(chance.numerator / chance.denominator * denominator) for chance in chances] + [denominator]
    return chances


if __name__ == '__main__':
    print('pass' if solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == [7, 6, 8, 21] else 'fail')
    print('pass' if solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == [0, 3, 2, 9, 14] else 'fail')
