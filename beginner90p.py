x = raw_input().rstrip()
digits = []
for m in x:
	if m.isdigit():
		digits.append(m)
print("".join(digits))
