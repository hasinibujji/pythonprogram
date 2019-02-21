n,m=map(int,raw_input().split())
p=int(n/2)
q=int(m**0.5)
if(p*2==n and q*q==m):
    print("yes")
else:
    print("no")
