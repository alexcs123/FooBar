def solution(total_lambs):
    fib, msb = 0, 0
    a, b = 1, 1
    lambs = total_lambs + 1

    while total_lambs > 0:
        total_lambs -= b
        fib += 1
        b += a
        a = b - a

    while lambs > 0:
        lambs = int(lambs / 2)
        msb += 1

    return fib - msb + 1


if __name__ == '__main__':
    tests = ((143, 3),
             (10, 1))

    for test, answer in tests:
        print('pass' if solution(test) == answer else 'fail')
