nums = [1,1,1,3,3,4,3,2,4,2]

def contains_duplicate(nums):
    nums = sorted(nums)
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return print(True)
    return print(False)


if __name__ == '__main__':
    contains_duplicate(nums)