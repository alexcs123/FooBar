def solution(l):
    doubles = [0] * len(l)
    triples = 0

    for i in range(len(l) - 2):
        for j in range(i + 1):
            doubles[i + 1] += 1 if l[i + 1] % l[j] == 0 else 0
            triples += doubles[j + 1] if l[i + 2] % l[j + 1] == 0 else 0

    return triples


if __name__ == '__main__':
    print('pass' if solution([1, 2, 3, 4, 5, 6]) == 3 else 'fail')
    print('pass' if solution([1, 1, 1]) == 1 else 'fail')
