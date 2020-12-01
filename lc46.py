"Given an array nums of distinct integers, return all the possible permutations."
"You can return the answer in any order."


def permute(nums: list) -> list:
    result = []

    def permute_helper(num, i, current):
        if len(nums) == i:
            result.append(current.copy())
        else:
            for j in range(i, len(num)):
                num[i], num[j] = num[j], num[i]
                current.append(num[i])
                permute_helper(num, i+1, current)
                current.pop()
                num[i], num[j] = num[j], num[i]

    permute_helper(nums, 0, [])

    return result


def main():
    print(permute([1, 2, 3]))
    return


if __name__ == '__main__':
    main()
