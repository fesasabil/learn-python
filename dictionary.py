# Dictionaries are another example of a data structure. A dictionary is used to map or associate things you want to store the keys you need to get them. A dictionary in Python is just like a dictionary in the real world. Python Dictionary are defined into two elements Keys and Values.

# Keys will be a single element
# Values can be a list or list within a list, numbers, etc.


# Syntax for Python Dictionary:
Dict = {'Saber': 20, 'Pharsya': 19, 'Gusion': 20}
print((Dict['Pharsya']))


# Python Dictionary Methods
Dict = {'Saber': 20, 'Pharsya': 19, 'Gusion': 20}
Dict.update({"Kagura": 21})
Dict['Kagura'] = 18
del Dict['Pharsya']
Boys = {'Saber': 20, 'Gusion': 20}
Girls = {'Pharsya': 19}
studentX=Boys.copy()
studentY=Girls.copy()
print(Dict)
print("Heros name : %s" % list(Dict.items()))
print(studentX)
print(studentY)

Dict = {'Saber': 20, 'Pharsya': 19, 'Gusion': 20}
Boys = {'Saber': 20, 'Gusion': 20}
Girls = {'Pharsya': 19}
for key in Boys.keys():
    if key in Boys.keys():
        print (True)
    else:
        print (False)

Dict = {'Saber': 20, 'Pharsya': 19, 'Gusion': 20}
Boys = {'Saber': 20, 'Gusion': 20}
Girls = {'Pharsya': 19}
Heros = list(Dict.keys())
Heros.sort()
for H in Heros:
    print(":".join((H,str(Dict[H]))))


# Python Dictionary in-built Functions
Dict = {'Saber': 20, 'Pharsya': 19, 'Gusion': 20}
print("Length : %d" % len (Dict))
print("variable Type: %s" %type (Dict))
print("printable string:%s" % str (Dict))