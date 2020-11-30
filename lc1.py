'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.'
'You may assume that each input would have exactly one solution, and you may not use the same element twice.'
'You can return the answer in any order.'


def twoSum(nums: list, target: int) -> list:
    index = -1
    candidate = []
    for i in nums:
        index += 1
        index_j = -1
        for j in nums:
            index_j += 1
            if index_j == index:
                pass
            else:
                if i + j == target:
                    candidate.append(index)
                    candidate.append(index_j)
                    return candidate


def main():
    print(twoSum([2, 7, 11, 15], 9))
    return


if __name__ == '__main__':
    main()
