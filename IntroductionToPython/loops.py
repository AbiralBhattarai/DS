count = 0
while(count<3):
    count+=1
    print("hello")
else:
    print("While loop exited. Now in else block")

print('Else block also exited now in main program flow')


#now lets look at a infinite while loop and how to use a termination condition to counteract it
c = 0
while(c>=0):
    c+=1
    print(c)
    
    if(c==3):               # this is the termination condition which breaks out of the infinite loop once c = 3
        break


#for loops
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i)

#loop control statements
#continue
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)
#break
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
    print('Current Letter :', letter)
#pass
for letter in 'geeksforgeeks':
    pass
print('Current Letter :', letter)