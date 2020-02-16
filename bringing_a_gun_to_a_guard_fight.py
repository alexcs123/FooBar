from math import ceil, sqrt, atan, pi


def answer(dimensions, your_position, guard_position, distance):
    repeats = [int(ceil(distance / dimension)) for dimension in dimensions]
    points = {}

    for position, guard in [(guard_position, True), (your_position, False)]:
        for xrepeat in range(-repeats[0], repeats[0] + 2):
            for yrepeat in range(-repeats[1], repeats[1] + 2):
                x = xrepeat * dimensions[0] - your_position[0] + (position[0] if xrepeat % 2 == 0 else dimensions[0] - position[0])
                y = yrepeat * dimensions[1] - your_position[1] + (position[1] if yrepeat % 2 == 0 else dimensions[1] - position[1])
                radius = sqrt(x ** 2 + y ** 2)

                if radius <= distance:
                    if x > 0:
                        angle = atan(y / x) if y > 0 else 2 * pi + atan(y / x)
                    elif x < 0:
                        angle = pi + atan(y / x)
                    else:
                        angle = pi / 2 if y > 0 else 1.5 * pi

                    points[angle] = (radius, guard) if not (angle in points and points[angle][0] < radius) else points[angle]

    return len([None for angle in points if points[angle][1]])


if __name__ == '__main__':
    print('success') if answer([3, 2], [1, 1], [2, 1], 4) == 7 else print('failure')
    print('success') if answer([2, 5], [1, 2], [1, 4], 11) == 27 else print('failure')
    print('success') if answer([23, 10], [6, 4], [3, 2], 23) == 8 else print('failure')
    print('success') if answer([10, 10], [4, 4], [3, 3], 5000) == 739323 else print('failure')
