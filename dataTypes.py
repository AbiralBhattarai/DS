#numeric data types
a = 5 #integer
b=5.0 #float
c = 3+2j #complex
print(a,b,c)
#Boolean
a = True
b = False
print (a or b)
print (a and b)
#Set
set1 = set()
set1 = set("AbiralDADA")
print(set1)
set1 = set([1,2,3,4,5])
print(set1)
set1 = set(["Geeks","for","Geeks"])
print(set1)
for item in set1:
    print(item)

#Dictionary
Dict = {}
Dict = {1:'Geeks',2:'For',3:"Geeks"}
print(Dict[2])

#String
s = "Abiral"
print(s[0],s[3])
s = "hello\nbud\nwussup"
print(s[0:5])

#Lists
L = []
L.append("Geeks")
print(L)
L =[[1,2,3,4],['geeks','for','geeks']]
print(L)
print(L[0][-1],L[-1][-2])

#Tuples
t = ()
t = ('Geeks','For')
print(t)
t = tuple("abiral")
print(t)
t1 = (1,2,3)
t2 = (3,4,5)
print(t1+t2)
t3 = (t1,t2)
print(t3)