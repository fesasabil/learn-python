# XML stands for eXtensible Markup Language. It was designed to store and transport small to medium amounts of data and is widely used for sharing structured information.

# Python enables you to parse and modify XML document. In order to parse XML document you need to have the entire XML document in memory. In this tutorial, we will see how we can use XML minidom class in Python to load and parse XML file.

import xml.dom.minidom
import xml.etree.ElementTree as ET


# def main():

#     doc = xml.dom.minidom.parse("Myxml.xml");

#     print(doc.nodeName)
#     print(doc.firstChild.tagName)

# if __name__=="__main__":
#     main()


def main():

    doc = xml.dom.minidom.parse("Myxml.xml")

    print(doc.nodeName)
    print(doc.firstChild.tagName)

    expertise = doc.getElementsByTagName("expertise")
    print ("%d expertise:" % expertise.length)
    for skill in expertise:
        print (skill.getAttribute("name"))

    # create a new XML tag and add it into the document
    newexpertise = doc.createElement("expertise")
    newexpertise.setAttribute("name", "BigData")
    doc.firstChild.appendChild(newexpertise)
    print(" ")

    expertise = doc.getElementsByTagName("expertise")
    print ("%d expertise:" % expertise.length)
    for skill in expertise:
        print (skill.getAttribute("name"))

if __name__ == "__main__":
    main()


# How to Parse XML using ElementTree
tree = ET.parse('items.xml')
root = tree.getroot()

# all items data
print('Expertise Data:')

for elem in root:
   for subelem in elem:
      print(subelem.text)
