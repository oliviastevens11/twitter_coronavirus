#!/usr/bin/env python3

# command line args
import matplotlib.pyplot as plt
import pandas as pd
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
top_10 = items[0:10]
top_10.reverse()
x_axis = [item[0] for item in top_10]
y_axis = [item[1] for item in top_10]

if args.input_path == 'reduced.country':
    x_axis2 = range(len(x_axis))
    plt.bar(x_axis2, y_axis)
    plt.xticks(x_axis2, x_axis)
    plt.ylabel('Count')
    plt.xlabel('Country')
    plt.savefig('Chart of Top 10 Countries: ' + args.key + '.png')
if args.input_path == 'reduced.lang':
    x_axis2 = range(len(x_axis))
    plt.bar(x_axis2, y_axis)
    plt.xticks(x_axis2, x_axis)
    plt.ylabel('Count')
    plt.xlabel('Language')
    plt.savefig('Chart of Top 10 Languages: ' + args.key + '.png')
