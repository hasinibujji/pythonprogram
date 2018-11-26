def f(number):
    if(number<=1):
        return number
    else:
        return (f(number-1)+f(number-2))
number=int(raw_input())
for i in range(1,number+1):
    print f(i),
