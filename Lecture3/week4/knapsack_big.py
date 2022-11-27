'''
This file describes a knapsack instance, and it has the following format:

[knapsack_size][number_of_items]

[value_1] [weight_1]

[value_2] [weight_2]

...

For example, the third line of the file is "50074 834558",
indicating that the second item has value 50074 and size 834558, respectively.
As before, you should assume that item weights and the knapsack capacity are integers.

This instance is so big that the straightforward iterative implemetation
uses an infeasible amount of time and space.
So you will have to be creative to compute an optimal solution.
One idea is to go back to a recursive implementation,
solving subproblems --- and, of course,
caching the results to avoid redundant work --- only on an "as needed" basis.
Also, be sure to think about appropriate data structures for storing
and looking up solutions to subproblems.
'''

import sys
from tqdm import tqdm


def knapsack_big(knapsack_size, items):
    table = [0] * (knapsack_size + 1)
    for item in tqdm(items, total=len(items)):
        for weight in range(knapsack_size, item[1] - 1, -1):
            table[weight] = max(
                table[weight], table[weight - item[1]] + item[0])
    return table[-1]


def main():
    with open(sys.argv[1]) as file:
        knapsack_size, number_of_items = map(int, file.readline().split())
        items = [tuple(map(int, line.split())) for line in file]
    print(knapsack_big(knapsack_size, items))


if __name__ == '__main__':
    main()
