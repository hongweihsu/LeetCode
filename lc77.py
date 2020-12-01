def combine(n: int, k: int):
    result = []
    combine_helper(n, 1, k, [], result)
    print(result)


def combine_helper(n, i, k, current, result):
    if len(current) == k:
        result.append(current.copy())
        return
    for i in range(i, n+1):
        current.append(i)
        combine_helper(n, i + 1, k, current, result)
        current.pop()


def main():
    combine(4, 2)


if __name__ == '__main__':
    main()
