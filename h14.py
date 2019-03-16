def permutation(lst1): 
    if len(lst1) == 0: 
        return []
    if len(lst1) == 1: 
        return [lst1]
    l = [] 
    for i in range(len(lst1)): 
       m = lst1[i] 
       remLst = lst1[:i] + lst1[i+1:] 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l
data = list('123') 
for p in permutation(data): 
    print p 
