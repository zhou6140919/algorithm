import numpy as np
from collections import defaultdict

data = open("jobs.txt").readlines()
n = int(data[0].strip())
weights = [int(line.strip().split()[0]) for line in data[1:]]
lengths = [int(line.strip().split()[1]) for line in data[1:]]

# print(n)
# print(weights[0], lengths[0])
# print(len(weights))
def algo1(weights, lengths):
    jobs = []
    for w, l in zip(weights, lengths):
        jobs.append([w, l, w - l])

    jobs = sorted(jobs, key=lambda x: (x[2], x[0]), reverse=True)

    completion = 0
    w_completion = 0
    for j in jobs:
        completion += j[1]
        w_completion += j[0] * completion

    print(f"1: {w_completion}")


def algo2(weights, lengths):
    jobs = []
    for w, l in zip(weights, lengths):
        jobs.append([w, l, w / l])

    jobs = sorted(jobs, key=lambda x: (x[2], x[0]), reverse=True)

    completion = 0
    w_completion = 0
    for j in jobs:
        completion += j[1]
        w_completion += j[0] * completion

    print(f"2: {w_completion}")


algo1(weights, lengths)
algo2(weights, lengths)
