number=int(raw_input(""))
count1=0
if number>0:
    for x in range(1,number+1):
        if number%x==0:
            print x,
