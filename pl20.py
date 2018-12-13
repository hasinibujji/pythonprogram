x1=raw_input()
y1=len(x1)
z1=list(x1)
for i in range(y1):
    z1[i]=ord(x1[i])+3
for j in range(y1):
    z1[j]=chr(z1[j])
print ''.join(z1)
