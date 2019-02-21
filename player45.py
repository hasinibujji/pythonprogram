n,m=map(int,raw_input().split())
p1=int(n/2)
q1=int(m**0.5)
if(p1*2==n and q1*q1==m):
    print("yes")
else:
    print("no")
