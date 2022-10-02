array = open('QuickSort.txt').readlines()
array = [int(i) for i in array]

# 162085
# 164123
# 138382

assert len(array) == 10000

num = [3, 4, 5, 1, 2]
count = 0


def find_median_idx(nums, a, b, c):
    ans = sorted([nums[a], nums[b], nums[c]])
    # print(ans)
    if ans[1] == nums[a]:
        return 0
    elif ans[1] == nums[b]:
        return 1
    else:
        return 2


def quicksort_1(nums, left_idx, right_idx, count):
    count += right_idx - left_idx
    median_idx = (right_idx + left_idx) // 2
    # nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]

    pivot_idx = find_median_idx(nums, left_idx, median_idx, right_idx)
    # print(pivot_idx)
    if pivot_idx == 1:
        pivot = nums[median_idx]
        nums[median_idx], nums[left_idx] = nums[left_idx], nums[median_idx]
    elif pivot_idx == 2:
        nums[right_idx], nums[left_idx] = nums[left_idx], nums[right_idx]

    pivot = nums[left_idx]

    # print(nums)

    i = left_idx + 1
    for j in range(left_idx + 1, right_idx + 1):
        if nums[j] < pivot:  # if nums[j] > pivot, then do nothing
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[left_idx], nums[i - 1] = nums[i - 1], nums[left_idx]
    # print(nums)
    if left_idx < (i - 2):
        nums, count = quicksort_1(nums, left_idx, i - 2, count)
    # print(nums)
    if right_idx > i:
        nums, count = quicksort_1(nums, i, right_idx, count)
    # print(nums)
    return nums, count


# print(quicksort_1(num, 0, len(num) - 1, count))
print(quicksort_1(array, 0, len(array) - 1, count))
