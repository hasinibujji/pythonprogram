b=int(input())
sum=0
while(b>0):
    n=int(b%10)
    sum=(n*n)+sum
    b=int(b/10)
print(sum)
