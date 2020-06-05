# What is Loop?
# Loops can execute a block of code number of times until a certain condition is met. Their usage is fairly common in programming. Unlike other programming language that have For Loop, while loop, dowhile, etc.

# What is For Loop?
# For loop is used to iterate over elements of a sequence. It is often used when you have a piece of code which you want to repeat "n" number of time.

# What is While Loop?
# While Loop is used to repeat a block of code. Instead of running the code block once, It executes the code block multiple times until a certain condition is met.

def main():
    x, y = 8, 9

    if (x < y):
        st = "x is less than y"
    print(st)

if __name__ == "__main__":
    main()


# def main():
#     x, y = 8, 8

#     if (x < y):
#         st = "x is less than y"

#     elif (x == y):
#         st = "x is same as y"
#     else:
#         st = "x is greater than y"
#     print(st)

# if __name__ == "__main__":
#     main()


# def main():
# 	x,y = 10,8
# 	st = "x is less than y" if (x < y) else "x is greater than or equal to y"
# 	print(st)
	
# if __name__ == "__main__":
# 	main()


# Nested IF Statement
total = 100
# country = "US"
country = "AU"
if country == "US":
    if total <= 50:
        print("Shipping Cost is $50")
    elif total <= 100:
        print("Shipping Cost is $25")
    elif total <= 150:
        print("Shipping Costs $5")
else:
        print("Free")
if country == "AU": 
	  if total <= 50:
	    print("Shipping Cost is  $100")
else:
	    print("FREE")


# Switch Statement
# def SwitchExample(argument):
#     switcher = {
#         0: " This is Case Zero ",
#         1: " This is Case One ",
#         2: " This is Case Two ",
#     }
#     return switcher.get(argument, "nothing")


# if __name__ == "__main__":
#     argument = 1
#     print SwitchExample(argument)

for i in range(1,6):
        for j in range(i):
            print("*",end=' ')
        print()


# While
x = 0
# define a while loop
while(x < 4):
    print(x)
    x = x+1

for x in range(2, 7):
    print(x)

# use a for loop over a collection
Months = ["Jan","Feb","Mar","Apr","May","June"]
for m in Months:
    print(m)

# use the break and continue statements
for x in range(10,20):
    # if (x == 15): break
    if (x % 2 == 0) : continue
    print(x)


# How to use "enumerate" function for "For Loop"
Months = ["Jan","Feb","Mar","Apr","May","June"]
for i, m in enumerate (Months):
    print(i,m)


for i in '123':
    print("qodr", i)