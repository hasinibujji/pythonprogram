n11=int(input())
if(n11>0 and (n11 & (n11-1))==0):
    print("0")
else:
    if(n11%2!=0):
        print("1")
    else:
        print("2")
