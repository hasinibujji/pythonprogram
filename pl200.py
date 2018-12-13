import sys, string, math
 
T1 = raw_input()
l = []
for b in T1 :
    if b not in l :
        l.append(b)
T12 = ''.join(l)
print(T12)
