m=raw_input("")
vowels=set('aeiou')
if not vowels.isdisjoint(m):
    print "yes"
else:
    print "no"
