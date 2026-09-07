# AI生成版本：两数之和，哈希表优化
def two_sum(nums, target):
    hashmap = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], index]
        hashmap[num] = index
    return []

if __name__ == "__main__":
    res = two_sum([2,7,11,15],9)
    print(res)
