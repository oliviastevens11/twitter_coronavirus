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
items_sorted = sorted(items, key=lambda x: x[1], reverse=True)
x_axis = [item[0] for item in items_sorted[:10]]
y_axis = [item[1] for item in items_sorted[:10]]
if args.input_path == 'reduced.country':
    data_frame = pd.DataFrame({"Country":x_axis,"Count":y_axis})
    df_sorted = data_frame.sort_values('Count')
    plt.bar(data_frame['Country'], data_frame['Count'])
    plt.title('Number of Times ' + args.key + ' Used')
    plt.ylabel('Count')
    plt.xlabel('Country')
    plt.savefig('Using Pandas pt. 5 Chart of Country: ' + args.key + '.png')
if args.input_path == 'reduced.lang':
    data_frame = pd.DataFrame({"Language":x_axis,"Count":y_axis})
    data_frame = data_frame.sort_values(by="Count", ascending=True)
    plt.bar(x_axis, y_axis, data=data_frame)
    plt.title('Number of Times ' + args.key + ' Used')
    plt.ylabel('Count')
    plt.xlabel('Language')
    plt.savefig('Chart of Language:' + args.key + '.png')
