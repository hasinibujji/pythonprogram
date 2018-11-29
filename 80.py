number=int(raw_input(""))
digits = []
while number > 0:
    r = number % 10
    if r & 1 != 0:
        digits.append(str(r))
    number=number/10
digits = reversed(digits)
print (" ".join(digits))
