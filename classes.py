# A class is a logical grouping of data and functions. it gives the freedom to create data structures that contains arbitrary content and hence easily accessible.

class myClass():
    def method1 (self):
        print ("Qodr")


class childClass(myClass):
    def method1(self):
        myClass.method1(self);
        print("childClass Method1")

    # def method2 (self, someString):
    #     print ("Software Testing:" + someString)

    def method2(self):
        print("childClass method2")

def main():
    # exercise the class methods
    # c = myClass()
    # c.method1()
    # c.method2(" Testing is fun")
    c2 = childClass()
    c2.method1()
    c2.method2()

if __name__ == "__main__":
    main()


# Python Constructors'
# A constructor is a class function that instantiates an object to predefined values.

class User:
    name = ""

    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("Welcome to guru99, " + self.name)

User1 = User("Alex")
User1.sayHello()


# input

# print("Silahkan masukan nama : ")
# nama = input()

# print(f"Hello {nama}, Selamat datang")

# print("Angka Pertama : ")
# a = int(input() )

# print("Angka Kedua : ")
# b = int(input() )

# hasil = a + b
# print(f"{a} + {b} = {hasil}")