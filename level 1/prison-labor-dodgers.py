def solution(x, y):
    return sum(x) - sum(y) if (x + y).count(sum(x) - sum(y)) == 1 else sum(y) - sum(x)


if __name__ == '__main__':
    print('pass' if solution([13, 5, 6, 2, 5], [5, 2, 5, 13]) == 6 else 'fail')
    print('pass' if solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]) == -4 else 'fail')
