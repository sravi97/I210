Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> -7 + -6 + -5 + -4 + -3 + -2 + -1
-28
>>> ((17*9) + (24*10) + (21*11) + (27*12)) / 89
10.651685393258427
>>> 2 ** -20
9.5367431640625e-07
>>> 4356 / 61
71.40983606557377
>>> 4365 % 61
34
>>> s = "goodbye"
>>> s[0] == "g"
True
>>> s[7] == "g"
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s[7] == "g"
IndexError: string index out of range
>>> s[6] == "g"
False
>>> s[0] == "g" and s[1] == "a"
False
>>> s[-2] == "x"
False
>>> s[3] == "d"
True
>>> s[0] == s[6]
False
>>> s[-4:]== "tion"
False
>>> a = 6
>>> b = 7
>>> c = (a + b) / 2
>>> c
6.5
>>> inventory = ["paper", "staples", "pencils"]
>>> first = "John" and middle = "Fitzgerald" and last = "Kennedy"
SyntaxError: can't assign to operator
>>> first= "John"
>>> middle = "Fitzgerald"
>>> last = "Kennedy"
>>> fullname = first + " " + middle + " " + last + " "
>>> fullname
'John Fitzgerald Kennedy '
>>> fullname = first + " " + middle + " " + last
>>> fullname
'John Fitzgerald Kennedy'
>>> 17 + -9 < 10
True
>>> len (middle)
10
>>> len (middle) > len (first) < len (last)
True
>>> len (inventory) > (len (fullname) * 5)
False
>>> c < 24
True
>>> a < 6.75 > b
False
>>> len (middle) > len (first) < len (last)
True
>>> len (inventory) = 0 or len (inventory) > 10
SyntaxError: can't assign to function call
>>> len (inventory) == 0 or len (inventory) > 10
False
>>> flowers = ["rose", "bougainvillea", "yucca", "marigold", "daylilly", "Lilly of the valley"]
>>> flowers
['rose', 'bougainvillea', 'yucca', 'marigold', 'daylilly', 'Lilly of the valley']
>>> "potato" in flowers
False
>>> thorny = thorny[0] + thorny [1] + thorny [2]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    thorny = thorny[0] + thorny [1] + thorny [2]
NameError: name 'thorny' is not defined
>>> thorny = flowers [0] + flowers [1] + flowers [2]
>>> thorny
'rosebougainvilleayucca'
>>> thorny = [flowers [0], flowers [1], flowers [2]]
>>> thorny
['rose', 'bougainvillea', 'yucca']
>>> poisonous =[flowers [-1]]
>>> poisonous
['Lilly of the valley']
>>> dangerous = thorny + poisonous
>>> dangerous
['rose', 'bougainvillea', 'yucca', 'Lilly of the valley']
>>> 
