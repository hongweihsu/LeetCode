'Write an algorithm to determine if a number n is "happy".'
'A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.'
'Return True if n is a happy number, and False if not.'


def isHappy(n: int) -> bool:
    n_sum = n
    history_sum = [n]

    while n_sum != 1:
        elements = list(str(n_sum))
        numerical_ele = []
        n_sum = 0
        index = 0
        for i in elements:
            numerical_ele.append(int(i))
            n_sum += numerical_ele[index] * numerical_ele[index]
            index += 1

        if n_sum in history_sum:
            return False
        else:
            history_sum.append(n_sum)

    return True


def main():
    print(isHappy(19))


if __name__ == '__main__':
    main()
