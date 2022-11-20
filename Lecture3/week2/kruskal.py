from tqdm import tqdm


data = open("clustering1.txt").readlines()
data = [[int(i) for i in x.strip().split()] for x in data]
data.pop(0)
reverse_data = [[edge[1], edge[0], edge[2]] for edge in data]
data = data + reverse_data
data = sorted(data, key=lambda x: x[2])
print(data[0])

vertices = {i: [i] for i in range(1, 501)}
k = 4

for edge in tqdm(data, total=len(data)):
    v1 = edge[0]
    v2 = edge[1]
    cost = edge[2]

    key1 = None
    key2 = None

    for key in vertices.keys():
        if v1 in vertices[key]:
            key1 = key

        if v2 in vertices[key]:
            key2 = key

    assert key1 is not None
    assert key2 is not None

    if key1 == key2:
        continue

    if len(vertices) == k:
        print(v1, v2)
        print(cost)
        break

    if len(vertices[key1]) >= len(vertices[key2]):
        vertices[key1].extend(vertices[key2])
        del vertices[key2]
    else:
        vertices[key2].extend(vertices[key1])
        del vertices[key1]
