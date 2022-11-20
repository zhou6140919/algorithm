from tqdm import trange

data = open('clustering_big.txt').readlines()
num, bit_num = data.pop(0).split()
print(num, bit_num)
data = [[int(j) for j in i.split()] for i in data]
print(data[0])


def hamming_distance(a, b):
    dist = 0
    for b1, b2 in zip(a, b):
        if b1 != b2:
            dist += 1
    return dist

k = 1

# too slow
for i in trange(len(data)):
    flag = False
    for j in range(len(data)):
        if i == j:
            continue
        dist = hamming_distance(data[i], data[j])
        if dist < 3:
            flag = True
            break
    if flag:
        continue
    else:
        k += 1
print(k)

