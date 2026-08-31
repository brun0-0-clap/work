def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            # 原题BUG：这里写 right[i]，正确是 right[j]
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

if __name__ == "__main__":
    import pdb
    pdb.set_trace()
    test_in = [3, 1, 4, 1, 5, 9, 2, 6]
    print(merge_sort(test_in))
