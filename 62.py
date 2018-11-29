x=raw_input()
"""if all(c in '01' for a in x):
    print "yes"
else:
    print "No"
    """
if not(x.translate(None,'01')):
    print "yes"
else:
    print "No"
