d="hello my name is himanshu".capitalize()
print(d) #phla word capital hoga

e="hello my name is himanshu".title() # sbhi words ke first letter capital mein
print(e)

f="hello my name is himanshu".upper() # upper case ein sare letters
print(f)

g="hello my name is himanshu".lower()  # sare letter lowercase mein
print(g)

h="HeLLo TherE".swapcase()  # jo upper mein wo lower and vice versa
print(h)

a="it is raining".count("i")
print(a)# i kitni bar aya


b="it is raining".count("x")
print(b)# output-> 0


b="it is raining".find("g")
print(b)


b="it is raining".index("raining")
print(b)

b="it is raining".endswith("ing")
print(b)

b="it is raining".startswith("ing")
print(b)


a="Hello my name is {} and I am {}".format("Saurabh", 22)
print(a)

                           #a index             0        1
a="Hello my name is {1} and I am {0}".format("Saurabh", 22)
print(a)


a="Hello my name is {name} and I am {age}".format(name = "Saurabh", age = 22)
print(a)


  # neeche with output hai bs dekh lo inhe

"FLAT20".isalnum() # Alphanumeric
True
"FLAT20&".isalnum()
False
"FLAT".isalpha() # Alphabetic
True
"FLAT20".isalpha()
False
"20".isdigit()

"who is the pm of india".split()
['who', 'is', 'the', 'pm', 'of', 'india']
"who is the pm of india".split("pm")
['who is the ', ' of india']
"who is the pm of india".split("i")
['who ', 's the pm of ', 'nd', 'a']


" ".join(['who', 'is', 'the', 'pm', 'of', 'india'])
'who is the pm of india'
"-".join(['who', 'is', 'the', 'pm', 'of', 'india'])
'who-is-the-pm-of-india'


"Hi my name is Saurabh".replace("Saurabh", "Siddhant")
'Hi my name is Siddhant'

name="        Saurabh         "
print(name.strip())



l=[1,2,3]
l.extend([2,"hello"])
print(l)