

array = open('IntegerArray.txt', 'r').readlines()
array = [int(i) for i in array]
# array = [1, 3, 5, 2, 4, 6]


def merge_sort(left, right):
    output = list()
    i, j = 0, 0
    num_inv = 0
    for index in range(len(left)+len(right)):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
            if i == len(left):
                output.extend(right[j:])
                break
        else:
            output.append(right[j])
            j += 1
            num_inv += len(left[i:]) if i < len(left) else 0
            if j == len(right):
                output.extend(left[i:])
                break
    return output, num_inv


def merge_count(a):
    if len(a) == 1:
        return a, 0
    else:
        left = a[:len(a)//2]
        right = a[len(a)//2:]
        # print('left:', left)
        # print('right:', right)
        left, num_inv_left = merge_count(left)
        right, num_inv_right = merge_count(right)
        output, num_inv_split = merge_sort(left, right)
        num_inv = num_inv_left + num_inv_right + num_inv_split
        return output, num_inv


results = merge_count(array)
print(len(array))
print(results[1])
