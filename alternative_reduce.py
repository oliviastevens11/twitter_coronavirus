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

# load each of the input paths
total = defaultdict(lambda: Counter())
for path in args.input_paths:
    with open(path) as f:
        tmp = json.load(f)
        for k in tmp:
            total[k] += tmp[k]

# write the output path
with open(args.output_path,'w') as f:
    f.write(json.dumps(total))

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

plt.figure(10,6)

#plot the line graphs
for i, hashtag in enumerate(args.hashtags):
    tweet_counts = []
    for day in range(1, 366):
        tweet_counts.append(total[hashtag][str(day)])
    plt.plot(range(1, 366), tweet_counts, label=hashtag)

plt.xlabel('Day of Year')
plt.ylabel('Number of Tweets')
plt.title('Tweets by Hashtag')
plt.legend()
plt.savefig(args.output_path, format = 'png')

