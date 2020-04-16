def main():
    x, y = 8, 9

    if (x < y):
        st = "x is less than y"
    print(st)

if __name__ == "__main__":
    main()


def main():
    x, y = 8, 8

    if (x < y):
        st = "x is less than y"

    elif (x == y):
        st = "x is same as y"
    else:
        st = "x is greater than y"
    print(st)

if __name__ == "__main__":
    main()


def main():
	x,y = 10,8
	st = "x is less than y" if (x < y) else "x is greater than or equal to y"
	print(st)
	
if __name__ == "__main__":
	main()


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
