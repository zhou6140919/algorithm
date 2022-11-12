from tqdm import trange

nums = open("2sum.txt").readlines()
nums = [int(i.strip()) for i in nums]
nums = set(nums)
nums = sorted(nums)

hash = {}
for i in nums:
    hash[i] = 1


def find_target(t):
    for i in hash:
        ti = t - i
        if ti in hash and ti != i:
            return 1

    return 0


count = 0
for i in trange(-10000, 10001):
    if find_target(i):
        count += 1

print(count)
