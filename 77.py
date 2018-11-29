number=int(raw_input(""))
count=0
if number>0:
    for i in range(1,number+1):
        if number%i==0:
            print i,
