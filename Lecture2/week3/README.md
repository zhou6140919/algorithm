# Week 3 Heaps & Balanced Binary Search Trees

## Data Structures

Point: organize data so that it can be accessed quickly and usefully.

Examples: lists, stacks, queues, heaps, search trees, hashtables, bloom filters, etc.

Why so many?: different data structures support different sets of operations => suitable for different types of tasks

### Taking It To The Next Level

LEVEL 0: what is a data structure?
LEVEL 1: cocktail party-level literacy
**LEVEL 2: this problem calls out for a heap (which data structure is the most appropriate one.)**
LEVEL 3: I only use data structures that I create myself

### Heaps

- heap is a container for objects that have keys
    - employer records, network edges, etc

INSERT: add a new object to a heap. $O(log n)$ ($n$ is the number of objects in heap)
EXTRACT-MIN: remove an object in heap with a minimum key value. (equally well maximum key value) $O(log n)$
HEAPIFY: n batched Inserts. $O(n)$
DELETE: $O(log n)$

#### Application: Sorting

Canonical use of heap: fast way to do repeated minimum computations.

Example: SelectionSort $O(n^2)$

HeapSort: 1. inset all n array elements into a heap. 2. EXTRACT-MIN to pluck out elements in sorted order.

Running time of HeapSort: $O(n log n)$

#### Application: Median Maintanence

2 heaps
