'Count the number of prime numbers less than a non-negative number, n.'


def countPrimes(n):

    if n <= 2:
        return 0

    prime = [True] * n
    prime[0] = False
    prime[1] = False
    for i in range(2, n//2+1):
        if prime[i] is True:
            for j in range(i * i, n, i):
                prime[j] = False

    count = 0
    for prime in prime:
        if prime is True:
            count += 1

    return count


def main():
    print(countPrimes(10))


if __name__ == '__main__':
    main()
