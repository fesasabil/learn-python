# Python Internet Access using Urllib.Request and urlopen()

# What is urllib?
# urllib is a Python module that can be used for opening URLs. It defines functions and classes to help in URL actions.

# With Python you can also access and retrieve data from the internet like XML, HTML, JSON, etc. You can also use Python to work with this data directly. In this tutorial we are going to see how we can retrieve data from the web. For example, here we used a guru99 video URL, and we are going to access this video URL using Python as well as print HTML file of this URL.

import urllib.request


webUrl = urllib.request.urlopen('https://www.youtube.com/user/guru99com')

print("result code: " + str(webUrl.getcode()))