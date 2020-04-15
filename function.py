# A Function in Python is used to utilize the code in more than one place in a program. It is also called method or procedures. Python provides you many inbuilt functions like print(), but it also gives freedom to create your own functions.


def func1():
    print("I am learning python function") # Significance of Indentation (Space) in Python
    print("Ok boss")

func1()


def square(x):
    return x*x

print(square(4))


# Arguments in Functions
def multiply(x,y):
    print(x*y)

multiply(2,8)

def multiply(x,y=0):
    return x*y

print(multiply(5, y=4))

def qodr(*args):
    print(args)

qodr(1,2,3,4,5)


def sum(a,b):
    print(f"{a}+{b}={a+b}")
sum(3.0,7.9)


# Python return statement
def func2(a):
    if a%2==0:
        return 0
    else:
        return 1
print(func2(7))

def sum2(a=5,b=9):
    return a+b
print(sum2(2,3))

print(sum2())

# Local Scope
def func3():
    z=7
    print(z)
print(func3())

# Global Scope
f=7
def func4():
    print(f)
print(func4())

#del func4() # deleting function

# Lifetime
# def func1():
#          counter=0
#          counter+=1
#          print(counter)
#     print(func1())

myvar=lambda a,b:(a*b)+2
print(myvar(3,5))

def facto(n):
  if n==1:
    return 1
  return n*facto(n-1)
print(facto(3))