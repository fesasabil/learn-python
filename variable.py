# Declare variable
a = 100
print(a)

# Re-declare variable
a = 'mantap'
print(a)

# Concatenate variable type string and number
a = "anak"
b = 99
print(a + str(b))

# local & global variables
def someFunction():
    global a
    print(a)
    a = 'I am learning python'
    # print(a)

someFunction()
print(a)