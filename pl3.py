b1=int(input())
sum=0
while(b1>0):
    n1=int(b1%10)
    sum=(n1*n1)+sum
    b1=int(b1/10)
print(sum)
