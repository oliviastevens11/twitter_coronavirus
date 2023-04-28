#!/usr/bin/env python3
import os
import json
import glob
from datetime import datetime

from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import argparse

# create argument parser
parser = argparse.ArgumentParser(description='Generate line plot for hashtags')
parser.add_argument('--key',required=True)
args = parser.parse_args()

files_input = glob.glob('outputs/geoTwitter20*.lang')
dataset = {}

# load each of the input paths
total = defaultdict(lambda: Counter())
for path in files_input:
    doyst = os.path.splitext(os.path.basename(path))[0][10:18]
    doy = datetime.strptime(doyst, '%y-%m-%d')
    with open(path) as f:
        tmp = json.load(f)
        for key in args.key.split(','):
            if key in tmp:
                if doy not in dataset:
                    dataset[doy] = defaultdict(int)
                dataset[doy][key] += sum(tmp[key].values())


dataset = dict(sorted(dataset.items()))
print(dataset)
for k in args.key:
    x = list(dataset.keys())
    y = [dataset[doy][k] for date in x]
    plt.plot(x,y,label=args.key)

plt.xlabel('Day of the year')
plt.ylabel('Number of tweets')
plt.legend()
plt.savefig('line_graph.png')
plt.show()
'''
# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--output_path',required=True)
args = parser.parse_args()

input_paths = glob.glob("outputs/*.json")
print(input_paths)
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

print("total=", total)
dataset = {}
for hashtag, counter in total.items():
    counts = [0]*365 # initialize count for each day of the year
    for day, count in counter.items():
        counts[day-1] = count
    dataset[hashtag] = counts
print(dataset)
for hashtag, counts in dataset.items():
    plt.plot(range(1,366), counts, label=hashtag)

plt.xlabel('Day of the year')
plt.ylabel('Number of tweets')
plt.savefig('Line Plot.png')

with open(args.output_path,'w') as f:
    f.write(json.dumps(total))
'''
