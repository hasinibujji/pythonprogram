k = raw_input().rstrip()
evens = oddk = ''
for i, n in enumerate(k):
	if i & 1 == 0:
		evens += n
	else:
		oddk += n
		
		print(evens + " " + oddk)
