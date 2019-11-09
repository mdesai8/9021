import sys
import os
import numpy as np
import collections
import itertools
try:
	filename = input('Please enter the name of the file you want to get data from:')
except:
    print('Sorry, there is no such file.')
    sys.exit()
height = []
heights = []
heightss = []
with open(filename) as f:
    height = [line.split() for line in f]
for i in height:
	for j in i:
		heights.append(int(j))

diff = []
arrgroup = []
remove = []
l = len(heights) 
for i in range(l):
        for j in range(i+1, l):
                d = abs(heights[j] - heights[i])
                diff.append(d)
m = collections.Counter(diff)
maxi  = m.most_common(1)[0][0]

diff1 = []
for i in range(len(heights)-1):
        diff1.append((heights[i+1] - heights[i]))
z = []
z = [(x[0], len(list(x[1]))) for x in itertools.groupby(diff1)]
longest = max(z, key=lambda x:x[1])[1]

pillars_removed = len(heights) - maxi - 1                                                  
if longest == len(heights):
    pillars_removed = 0
if pillars_removed == 0:
    print('The ride is perfect!')
else:
    print('The ride could be better...')

print(f'The longest good ride has a length of: {longest}')
print(f'The minimal number of pillars to remove to build a perfect ride from the rest is: {pillars_removed}')
