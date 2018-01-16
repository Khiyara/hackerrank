#!/bin/python3

import sys


n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = int(input().strip())
   unsorted.append(unsorted_t)
unsorted.sort()
print "\n".join(str(x) for x in unsorted)
