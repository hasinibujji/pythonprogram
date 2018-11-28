x=int(raw_input())
y=[]
while(x>0):
    dig=x%10
    y.append(dig)
    x=x//10
print sum(y)
