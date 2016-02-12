#!/usr/bin/python
import sys

# Usage:
# 	python hmmss2seconds.py [hour] [min] [seconds]
result = (int(sys.argv[1]) * 3600) + ( int(sys.argv[2]) * 60) + int(sys.argv[3])

print( "%s:%s:%s = %s seconds" % (sys.argv[1], sys.argv[2], sys.argv[3], result) )