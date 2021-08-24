s = 'abcdefghijklmnopqrstuvwxyz'

#a)
if s[1:3] == 'bc':
    print(True)
else:
    print(False)

#b)
if s[:14] == 'abcdefghijklmn':
    print(True)
else:
    print(False)

        
if s[14:] == 'opqrstuvwxyz':
    print(True)
else:
    print(False)

#c)
if s[1:-1] == 'bcdefghijklmnopqrstuvw':
    print(True)
else:
    print(False)
