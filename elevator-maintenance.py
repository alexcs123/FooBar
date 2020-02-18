def solution(l):
    for i, version in enumerate(l):
        l[i] = [int(part) for part in (version + '.0.0').split('.')]
        l[i].append(len(version))

    for i, version in enumerate(sorted(l, key=lambda x: (x[0], x[1], x[2], x[-1]))):
        strung = ''

        for number in version[:-3]:
            strung += str(number) + '.'

        l[i] = strung[:-1]

    return l


if __name__ == '__main__':
    print('pass' if solution(['1.11', '2.0.0', '1.2', '2', '0.1', '1.2.1', '1.1.1', '2.0']) == ['0.1', '1.1.1', '1.2', '1.2.1', '1.11', '2', '2.0', '2.0.0'] else 'fail')
    print('pass' if solution(['1.1.2', '1.0', '1.3.3', '1.0.12', '1.0.2']) == ['1.0', '1.0.2', '1.0.12', '1.1.2', '1.3.3'] else 'fail')
