def solution(n):
    primes = []
    primestring = '2'
    candidate = 3

    while len(primestring) < n + 5:
        prime = True

        for divisor in primes:
            if candidate % divisor == 0:
                prime = False
                break

        if prime:
            primes.append(candidate)
            primestring += str(candidate)

        candidate += 2

    return primestring[n:n + 5]


if __name__ == '__main__':
    tests = ((0, '23571'),
             (3, '71113'))

    for test, answer in tests:
        print('pass' if solution(test) == answer else 'fail')
