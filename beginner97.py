num1=int(raw_input())
rev=0
while(num1>0):
 r=num1%10
 rev=rev*10+r
 num1=num1//10
print rev
