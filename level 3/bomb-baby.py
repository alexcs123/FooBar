def solution(m, f):
    m, f = int(m), int(f)
    cycles = 0

    while m != 1 or f != 1:
        if m > f:
            cycles += 1 if m / f == 1 else m / f - 1
            m -= f * (1 if m / f == 1 else m / f - 1)
        elif f > m:
            cycles += 1 if f / m == 1 else f / m - 1
            f -= m * (1 if f / m == 1 else f / m - 1)
        else:
            return 'impossible'

    return str(cycles)


if __name__ == '__main__':
    print('pass' if solution('4', '7') == '4' else 'fail')
    print('pass' if solution('2', '1') == '1' else 'fail')
