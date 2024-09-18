def add(num1: int, num2: int) -> int:
    num3 = num1 + num2

    return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

#we can write it also as
def add1(num1,num2):
    num3 = num1+num2
    return num3

num1,num2 = 5,15
print(add1(num1,num2))


def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

evenOdd(2)
evenOdd(3)

# default arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

#Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)


# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)


# You will get correct output because 
# argument is given in order
print("Case-1:")
nameAge("abiral", 22)
# You will get incorrect output because
# argument is not in order
print("\nCase-2:")
nameAge(22, "abiral")

#Arbitrary keyword arguments
def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

def evenOdd(x):
    """Function to check if the number is even or odd"""
    
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


# Driver code to call the function
print(evenOdd.__doc__)


def cube(x): return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))
print(cube_v2(7))


def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))