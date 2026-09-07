# 手动实现：两数之和
def two_sum(nums, target):
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

if __name__ == "__main__":
    res = two_sum([2,7,11,15],9)
    print(res)
