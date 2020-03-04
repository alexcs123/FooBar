def solution(n):
    n = int(n)
    operations = 0

    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n += 1 if (n + 1) % 4 == 0 and n != 3 else -1

        operations += 1

    return operations


if __name__ == '__main__':
    print('pass' if solution('15') == 5 else 'fail')
    print('pass' if solution('4') == 2 else 'fail')
