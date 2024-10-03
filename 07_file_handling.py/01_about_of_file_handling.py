                    # Some keypoints  
"""
r == read
a == append(add some data)
w == overwrite(remove last data and write some new data)
r+ == read + overwrite form starting
a+ == read + append form last
w+ == clear the data +read(not working because there is not data) + overwrite
"""

                    # File handling :- Work on the file

'''-----------------Open file :- syntax-----------------'''

# variable_Name :- open("File_Name","mode")
# example :  
# f = open("myLaptopPassword.txt","r")


'''-----------------Read file :- syntax-----------------'''

# variable.read("text")
# example :  
# myLaptopPassword.read()


'''-----------------Create file :- Syntax-----------------'''

# variable_Name :- open("filename.ectension","filemode")
# example :  
# myLaptopPassword = open("myLaptopPassword.txt","w") 


'''-----------------Write file :- syntax-----------------'''

# variable.write("text")
# example :  
# myLaptopPassword.write("tanya")


'''-----------------Delete file :- syntax-----------------'''

# import os
# example :  
# myLaptopPassword.write("tanya")  os.remove("password.txt")
