lower,upper=map(int,raw_input().split())
count=0
for number in range(lower,upper+1):
    if number>1:
        for x in range(2,number):
            if(number%x==0):
                break
        else:
          count=count+1
print (count) 
