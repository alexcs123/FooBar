def solution(src, dest):
    moves = 0
    discovered = [src]

    while dest not in discovered:
        new = []

        for square in discovered:
            candidates = ((square + 6, square % 8 >= 2), (square + 15, square % 8 >= 1), (square + 17, square % 8 <= 6), (square + 10, square % 8 <= 5), (square - 6, square % 8 <= 5), (square - 15, square % 8 <= 6), (square - 17, square % 8 >= 1), (square - 10, square % 8 >= 2))
            new += [candidate for candidate, allowed in candidates if allowed and 0 <= candidate <= 63]

        discovered = list(set(new))
        moves += 1

    return moves


if __name__ == '__main__':
    print('pass' if solution(0, 1) == 3 else 'fail')
    print('pass' if solution(19, 36) == 1 else 'fail')
