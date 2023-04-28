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

files_input = glob.glob('outputs/geoTwitter20*.country')
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

x_axis = []
y_axis = []
dataset = dict(sorted(dataset.items()))

for date, data in dataset.items():
    num_tweets = sum(data.values())
    if num_tweets > 0:
        x_axis.append(date)
        y_axis.append(num_tweets)
        x_axis = [doy.date() for date in x_axis]
print(x_axis)
print(y_axis)
plt.plot(x_axis, y_axis)

plt.xlabel('Day of the year')
plt.ylabel('Number of tweets')
plt.legend()
plt.savefig('_please_work_lol__.png')
''' 
keys = list(keys)

for k in keys:
    x_axis = list(dataset.keys())
    y_axis = [dataset[doy][k] for doy in x_axis]
    x_axis = [doy.date() for date in x_axis]
    x_axis = [doy.strftime("%m/%d/%Y") for doy in x_axis]
    print('x-axis=',x_axis)
    print('y-axis=', y_axis)
    plt.plot(x_axis, y_axis)
x_axis = list(dataset.keys())
x_axis = [doy.date() for date in x_axis]
keys = list(dataset[x_axis[0]].keys()) 

for k in keys:
    y_axis = [dataset[doy][k] for doy in x_axis]
    plt.plot(x_axis, y_axis, label=k)

print(y_axis)
plt.xlabel('Day of the year')
plt.ylabel('Number of tweets')
plt.legend()
plt.savefig('_please_work_lol.png')
'''
