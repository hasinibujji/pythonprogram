p=int(raw_input())
if p>1:
    for a in range(2,p):
        if p%a==0:
            print "no"
            break
    else:
            print "yes"
