num=int(input("enter a number"))
if(num<0):
	print("the number is negative")
elif(num==0):
	print("the sum is zero")
else:
	sum=num*(num+1)/2
	print("the sum of numbers is",num)
