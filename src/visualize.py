#!/usr/bin/env python3

# command line args
import matplotlib.pyplot as plt
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

#print graphs of values
x_axis = [item[0] for item in items[:9]]
y_axis = [item[1] for item in items[:9]]
plt.bar(x_axis, y_axis)
plt.title('Count of the Number of Times Coronavirus is used')
plt.xlabel('Language')
plt.ylabel('Count')
plt.savefig('Corona.png')
