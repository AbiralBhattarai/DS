print('Hello world')

#Lists
num = []
num.append(21)
num.append(40.5)
num.append("String")
print(num)

#this is a single line comment
""" this is a
    multi line comment """
# taking inputs

#by default, inputs return string
name = input("Enter name ")
print(name,type(name))

#to take anyother data type as input, specify it while taking input in the following way
num = int(input("Enter a num "))
print(num,type(num))

#if elif else
num = 10
if(num>12):
    print("Good")
elif(num>20):
    print("Not Good")
else:
    print("Great")

#to define functions in python, we use the def keyword
def hello(count):
    print("Hello")
    print("Hello world")
    #hello() 
    count+=1
    """this causes infinite recursions 
    so, we dont use it or we add a base condition"""
    if (count == 5):
        exit
    else:
        hello(count)
#calling the function
hello(0)

#Similar to other programming languages, python also has Main func
import random
import math
def getInt():
    return random.randint(1,100)

def Main():
    print("Started Main")
    print(getInt())
    num =-85
    num = math.fabs(num)
    print(int(num))

if __name__ == "__main__":
    Main()