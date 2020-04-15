# TUPLE
#   A tuple is just like a list of a sequence of immutable python objects. The difference between list and tuple is that list are declared in square brackets and can be changed while tuple is declared in parentheses and cannot be changed. However, you can take portions of existing tuples to make new tuples.

# Tuple Assignment

tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1,2,3,4,5,6,7);
print(tup1[1])
print(tup2[1:4])

# Packing and Unpacking
x = ("Python", 20, "Education") # tuple packing
(company, emp, profile) = x # tuple unpacking
print(company)
print(emp)
print(profile)

# Comparing tuples
a = (5,6)
b = (6,4)
if (a>b):print("a is bigger")
else: print("b is bigger")

# Using tuples as keys in dictionaries
a = {'x':100, 'y':200}
b = list(a.items())
print(b)

# Slicing of Tuple
x = ("a", "b","c", "d", "e")
print (x[2:4])