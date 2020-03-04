def solution(l):
    over = [number for number in sorted(l) if number % 3 == 1]
    under = [number for number in sorted(l) if number % 3 == 2]

    if sum(l) % 3 == 1 and len(over) >= 1:
        l.remove(over[0])
    elif sum(l) % 3 == 1 and len(under) >= 2:
        l.remove(under[0])
        l.remove(under[1])
    elif sum(l) % 3 == 2 and len(under) >= 1:
        l.remove(under[0])
    elif sum(l) % 3 == 2 and len(over) >= 2:
        l.remove(over[0])
        l.remove(over[1])

    return int('0' + ''.join(map(str, reversed(sorted(l)))))


if __name__ == '__main__':
    print('pass' if solution([3, 1, 4, 1]) == 4311 else 'fail')
    print('pass' if solution([3, 1, 4, 1, 5, 9]) == 94311 else 'fail')
