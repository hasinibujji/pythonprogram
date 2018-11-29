number=int(raw_input(""))
count=0
if number>1:
    for i in range(2,number):
        if number%i==0:
            count=count+1
if count>1:
    print "yes"
else:
    print "no"
