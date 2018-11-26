string=raw_input()
character=0
word=0
for i in string:
    character=character+1
    if(i==' '):
        word=word+1
print(character-word),
