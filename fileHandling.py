import os
from os import path

# How to Create a Text File
# def main():
#     f = open("guru.txt", "w+")

#     for i in range(10):
#         f.write("This is line %d\r\n" % (i+1))

#     f.close()

# if __name__=="__main__":
#     main()


# How to Append Data to a File
# def main():
#     f = open("guru.txt", "a+")

#     for i in range(2):
#         f.write("Append line %d\r\n" % (i+1))

#     f.close()

# if __name__=="__main__":
#     main()


# How to Read a File
# def main():
#     f = open("guru.txt", "r")
#     if f.mode == "r":
#         contents = f.read()
#         print(contents)

# if __name__=="__main__":
#     main()


# How to Read a File line by line
def main():
    f = open("guru.txt", "r")
    f1 = f.readlines()
    for x in f1:
        print(x)

if __name__=="__main__":
    main()


# File Modes in Python

# Mode	Description

# 'r'	    This is the default mode. It Opens file for reading.
# 'w'	    This Mode Opens file for writing.
# If file does not exist, it creates a new file.
# If file exists it truncates the file.
# 'x'	    Creates a new file. If file already exists, the operation fails.
# 'a'	    Open file in append mode.
# If file does not exist, it creates a new file.
# 't'	    This is the default mode. It opens in text mode.
# 'b'	    This opens in binary mode.
# '+'	    This will open a file for reading and writing (updating)


# Rename File and Directory using os.rename()
# def main():
#     # make a duplicate of an existing file
#     if path.exists("guru.txt"):
#         # get the path to the file in the current directory
#           src = path.realpath("guru.txt")

#         # rename the original file
#         os.rename('guru.txt', 'guru99.txt')

# if __name__=="__main__":
#     main()