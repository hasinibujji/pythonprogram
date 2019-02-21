k,n=map(int,raw_input().split())
def gcd(x,y):
    z=abs(x-y)
    if (x-y)==0:
        return y
    else:
        return gcd(z,min(x,y))
print gcd(k,n)
 
