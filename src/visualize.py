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
items_sorted = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
top_10 = items_sorted[:10]
print(top_10)
x_axis = [item[0] for item in top_10]
y_axis = [item[1] for item in top_10]
print("x_axis=", x_axis)
print("y_axis=", y_axis)
fig, ax = plt.subplots()
ax.bar(x_axis, y_axis)

# set plot title and axis labels
ax.set_title('Number of Times ' + args.key + ' Used')
ax.set_ylabel('Count')
ax.set_xlabel('Country')

# save the plot to a file
plt.savefig('Chart 12345 of Country: ' + args.key + '.png')

'''
if args.input_path == 'reduced.country':
    df = pd.DataFrame(top_10, columns=['Country', 'Count'])
    sns.barplot(x='Country', y='Count', data=df, order=df.sort_values('Count')['Country'])
    #plt.bar(x_axis, y_axis)
    plt.title('Number of Times ' + args.key + ' Used')
    plt.ylabel('Count')
    plt.xlabel('Country')
    plt.savefig('Chart 22 of Country: ' + args.key + '.png')
if args.input_path == 'reduced.lang':
    data_frame = pd.DataFrame({"Language":x_axis,"Count":y_axis})
    df_sorted = data_frame.sort_values('Count')
    plt.bar(df_sorted['Country'], df_sorted['Count'])
    plt.title('Number of Times ' + args.key + ' Used')
    plt.ylabel('Count')
    plt.xlabel('Language')
    plt.savefig('Chart of Language:' + args.key + '.png')
'''
