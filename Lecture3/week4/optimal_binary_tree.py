'''
Optimal Binary Search Tree Problem
Dynamic Programming
'''


def optimal_binary_tree(keys, freq):
    '''
    Optimal Binary Search Tree Problem
    Dynamic Programming
    '''
    n = len(keys)
    cost = [[0 for _ in range(n)] for _ in range(n)]
    root = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]
        root[i][i] = i

    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            cost[i][j] = float('inf')
            for r in range(i, j+1):
                c = ((cost[i][r-1] if r > i else 0) +
                     (cost[r+1][j] if r < j else 0) + sum(freq[i:j+1]))
                if c < cost[i][j]:
                    cost[i][j] = c
                    root[i][j] = r

    return cost, root


def print_optimal_bst(root, i, j, parent, is_left):
    '''
    Print Optimal BST
    '''
    if i > j:
        return
    print('k{} is the {} child of k{}'.format(
        root[i][j], 'left' if is_left else 'right', parent))
    print_optimal_bst(root, i, root[i][j]-1, root[i][j], True)
    print_optimal_bst(root, root[i][j]+1, j, root[i][j], False)


def main():
    '''
    Main function
    '''
    keys = [1, 34, 33, 32]
    freq = [1, 2, 3, 4]
    cost, root = optimal_binary_tree(keys, freq)
    print_optimal_bst(root, 0, len(keys)-1, -1, False)


if __name__ == '__main__':
    main()
