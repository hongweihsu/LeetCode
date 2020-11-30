'Count the number of prime numbers less than a non-negative number, n.'


# brute force
def main(n):
    count = 0
    if n <= 2:
        return 0

    for i in range(2, n):  # 0,1,2,3,4,5  n=6
        if is_prime(i):
            print('prime:', i)
            count += 1
    print(count)
    return count


def is_prime(n):
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# # dynamic
def main2(n, count_prime):
    if n == 0:
        count_prime.append(0)
        return count_prime[n]
    if n >= 1:
        main2(n - 1, countPrime)
        countPrime.append(countPrime[n - 1] + check_prime(n))
        print(n, count_prime)
        return count_prime[n]


def check_prime(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1

    for i in range(2, n):
        if n % i == 0:
            return 0
        if i == n - 1:
            return 1


def main3(n):
    countPrime = [0, 0]
    if n <= 1:
        return countPrime[n]
        # return 0
    elif n == 2:
        countPrime.append(0)
        return countPrime[n]
    for i in range(n):
        if i <= 1:
            pass
        else:
            if n % i == 0:
                countPrime.append(countPrime[n - 1])
                break
    return countPrime.append(countPrime[n - 1] + 1)


def main4(n):
    prime = []
    if n <= 2:
        return 0

    for i in range(2, n):
        if isis_prime(i, prime):
            prime.append(i)
    print('prime:', prime)
    print(len(prime))


def isis_prime(n, prime):
    if n == 2:
        return True

    for i in prime:
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    # brute force
    # main(10)

    # dynamic
    # n = 1
    # countPrime = []
    # main2(n, countPrime)
    # if is_prime(n):
    #     print(countPrime[n]-1)
    # else:
    #     print(countPrime[n])

    # print(main3(10))

    main4(100)
