import math
m,n=map(int,raw_input().split())
b=m * n
if math.sqrt(b).is_integer():
    print "yes"
else:
    print "no"
