list = int(raw_input())
num = [1,2,3]
num.sort()
length = len(num)
if (length % 2 == 0):
    mid = (num[(length)//2] + num[(length)//2-1]) / 2
else:
    mid = num[(length-1)//2]
print(mid)
