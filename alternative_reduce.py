#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--output_path',required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

# load each of the input paths
total = defaultdict(lambda: Counter())
for path in args.input_paths:
    with open(path) as f:
        tmp = json.load(f)
        for k in tmp:
            total[k] += tmp[k]

dataset = {}
for hashtag, counter in total.items():
    counts = [0]*365 # initialize count for each day of the year
    for day, count in counter.items():
        counts[day-1] = count
    dataset[hashtag] = counts

for hashtag, counts in dataset.items():
    plt.plot(range(1,366), counts, label=hashtag)

plt.xlabel('Day of the year')
plt.ylabel('Number of tweets')
plt.savefig('Line Plot')

with open(args.output_path,'w') as f:
    f.write(json.dumps(total))
