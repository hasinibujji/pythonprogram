x=int(raw_input())
reverse=0
while(x>0):
    remainder=x%10
    reverse=reverse*10+remainder
    x=x/10
print reverse  
