#List are mutable(Chnage kr skte hai)->denoted by []
#Tuples are Immutable(Changes ni kr skte)-> denoted by ()


l=[1,1,2,2,3,3,4,4]
l1=[]

for i in l:
    if i not in l1:
        l1.append(i)
print(l1)