var1 = "python!"
var2 = "Programmer league"
print ("var1[0]:",var1[0])
print ("var2[1:5]:",var2[1:5])
print ("y" in  var1)
print ("p" not in var1)
print (f"Hello {var1} {var2}") # string format

name = 'python'
number = 99
print ('%s %d' %(name, number))

x = "Guru"
y = "99"
print (x*2)

# Python String replace() Method
oldstring = 'I like you'
newstring = oldstring.replace('like', 'love')
print(newstring)

# Changing upper and lower case strings
string = 'python at mama'
print(string.upper())
print(string.capitalize())
print(string.lower())

# Using "join" function for the string
print(":".join("Python"))

# Reversing String
string="12345"		
print(''.join(reversed(string)))

# split strings
word="guru99 career guru99"		
print(word.split(' '))
print(word.split('r'))