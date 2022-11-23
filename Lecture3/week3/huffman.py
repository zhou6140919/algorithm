'''
第 1 个问题
In this programming problem and the next you'll code up the greedy algorithm from the lectures on Huffman coding.

Download the text file below.

This file describes an instance of the problem. It has the following format:

[number_of_symbols]

[weight of symbol #1]

[weight of symbol #2]

...

For example, the third line of the file is "6852892," indicating that the weight of the second symbol of the alphabet is 6852892.  (We're using weights instead of frequencies, like in the "A More Complex Example" video.)

Your task in this problem is to run the Huffman coding algorithm from lecture on this data set. What is the maximum and minimum length of a codeword in the resulting Huffman code?
'''

import sys
import heapq


class Node:
    def __init__(self, weight, left=None, right=None):
        self.weight = weight
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return 'Node(weight=%s, left=%s, right=%s)' % (self.weight, self.left, self.right)


def huffman(nodes):
    heapq.heapify(nodes)
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        heapq.heappush(nodes, Node(left.weight + right.weight, left, right))
    return nodes[0]


def max_length(node, length=0):
    if node.left is None and node.right is None:
        return length
    return max(max_length(node.left, length + 1), max_length(node.right, length + 1))


def min_length(node, length=0):
    if node.left is None and node.right is None:
        return length
    return min(min_length(node.left, length + 1), min_length(node.right, length + 1))


def main():
    with open(sys.argv[1]) as f:
        n = int(f.readline())
        nodes = [Node(int(f.readline())) for _ in range(n)]
    print(max_length(huffman(nodes)))
    print(min_length(huffman(nodes)))


if __name__ == '__main__':
    main()
