n1,k1,p1=map(int,raw_input().split())
if(n1+k1<=p1 or k1+p1<=n1 or p1+n1<=k1):
    print "no"
else:
    print "yes"
