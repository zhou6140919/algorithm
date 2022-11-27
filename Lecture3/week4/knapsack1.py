'''
This file describes a knapsack instance, and it has the following format:

[knapsack_size][number_of_items]

[value_1] [weight_1]

[value_2] [weight_2]

...

For example, the third line of the file is "50074 659",
indicating that the second item has value 50074 and size 659, respectively.

You can assume that all numbers are positive.
You should assume that item weights and the knapsack capacity are integers.
'''

import sys


def knapsack1(knapsack_size, items):
    table = [[0 for _ in range(knapsack_size + 1)]
             for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        for j in range(1, knapsack_size + 1):
            if items[i - 1][1] > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(table[i - 1][j], table[i - 1]
                                  [j - items[i - 1][1]] + items[i - 1][0])
    return table[-1][-1]


def main():
    with open(sys.argv[1], 'r') as input_data:
        knapsack_size, number_of_items = map(
            int, input_data.readline().split())
        items = []
        for line in input_data.readlines():
            items.append(tuple(map(int, line.split())))
    print(knapsack1(knapsack_size, items))


if __name__ == '__main__':
    main()
