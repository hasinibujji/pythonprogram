def play_31():
	s1=(raw_input())
	x1,x2=0,0
	for i in s1:
		if i=='(':
			x1+=1
		if i==')':
			x2+=1
	if x1==x2:
		print('yes')
	else :
		print('no')
play_31()
		
