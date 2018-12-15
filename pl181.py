def isSum(x,y,z):
    if y<z:
        z,y=y,z
    while x>=0:
        if x%y==0:
            return True
        x-=z
    return False
 
x = int(input())
if isSum(x,3,7):
    print("yes")
else:
	print("no")
