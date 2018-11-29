number=int(raw_input(""))
digits = []
while number > 0:
    s = number % 10
    if s & 1 != 0:
        digits.append(str(s))
    number=number/10
digits = reversed(digits)
print (" ".join(digits))
