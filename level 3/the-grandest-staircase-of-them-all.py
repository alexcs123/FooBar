def solution(n):
    partitions = [1, 1] + [0] * (n - 1)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            partitions[n - j] += partitions[n - j - i - 2]

    return partitions[n] - 1


if __name__ == '__main__':
    print('pass' if solution(200) == 487067745 else 'fail')
    print('pass' if solution(3) == 1 else 'fail')
