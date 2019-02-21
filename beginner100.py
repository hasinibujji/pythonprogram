num1=int(raw_input())
def calcProduct(num1):
	if(len(str(num1)) == 1):
		return num1
	else:
		return (num1%10 * calcProduct(num1/10))
print(calcProduct(2143))
