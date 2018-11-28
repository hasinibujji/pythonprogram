p,q=map(int,raw_input().split())
list=[int(a) for a in raw_input().split()]
if q in list:
    count=list.count(q)
    print count
else:
    print 0
