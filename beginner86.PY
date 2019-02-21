# your code goes here
def isIsogram(k1):
	charMap = {}
	for n in k1:
		if n in charMap:
			return False
		else:
			charMap[n] = 1
	return True
k1 = raw_input().rstrip()
print("Yes" if isIsogram(k1) else "No")
