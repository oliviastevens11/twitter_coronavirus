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

dataset = dict(sorted(dataset.items()))
for doy, tmp in dataset.items():
    keys = set()
    keys.update(tmp.keys())
    keys = list(keys)

for k in keys:
    x_axis = list(dataset.keys())
    y_axis = [dataset[doy][k] for doy in x_axis]
    x_axis = [doy.date() for doy in x_axis]
    plt.plot(x_axis,y_axis,label=args.key)

plt.xlabel('Day of the year')
plt.ylabel('Number of tweets')
plt.legend()
plt.savefig('__line__graph__.png')

plt.show()
