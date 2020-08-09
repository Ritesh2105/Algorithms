nums = [4, 1, 2, 1, 2]


def single_number(nums):
    count = 0
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1):
            if nums[i] == nums[j]:
                count += 1
        if count == 2:
            print(count)
            print(nums[i])


if __name__ == '__main__':
    single_number(nums)
