def rat(x,y):
    print(x[y:]+x[:y])
x,y=map(str,raw_input().split())
y=int(y)

k=len(x)-y
rat(x,k)
