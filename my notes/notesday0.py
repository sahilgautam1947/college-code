# # print(<expression>) 
# # it is a command used to print any thing in python_branch

# #  In Python code, a string is always enclosed in quotation marks. However, the print function displays a string without
# # the quotation marks.

# from pdb import line_prefix


# You can also write a print function that includes two or more expressions separated by commas

# The syntax for a print statement with two or more expressions looks like the following:
# print(<expression>,..., <expression>)

# Note the ellipsis (...) in this syntax example. The ellipsis indicates that you could include multiple expressions after the first one. 

# Whether it outputs one or multiple expressions, the print function always ends its output with a newline
# this means that the curser at the end of the programm would end up in a new line or the next line 


# To begin the next output on the same line as the previous one, you can place the expression end = "", which says “end the line with an empty string instead of a newline,” at the end of the list of expressions, as follows:
# print(<expression>, end = "")


name = input("Enter your name: ")   
# here the input is a function that takes an input and to take that input it shows the prompt which is written in the input function  
# then on the left you assign the variable in which you want to store the return value and thats it you got the input and stored it

# >>> name = input("Enter your name: ")   
# Enter your name: 22265
# >>> name
# '22265'
# >>> print(name) 
# 22265
# >>>


name = input(55)   
# this also works
# >>> name = input(55)   
# 55sahil
# >>> name
# 'sahil'
# >>> print(name) 
# sahil
# >>>

name = input(  )   
# this also works
# >>> name = input(  )
# sahil
# >>> print(name)
# sahil
name = input()
# and this also works
# >>> name = input()
# sahil
# >>> print(name)
# sahil

name = input("Enter your name: ")   
# >>> name = input("Enter your name: ")   
# Enter your name: sahil
# >>> name
# 'sahil'
# >>>

# if you declared a string as a variable then you need not use"" as it is a variable 



# i want this programm to run 
# a=input("length of rectangle") 
# b=20
# p= a*b



# whats wrong with this code 
# a=464466
# b=input("second number")
# print(a+b)

length=int(input("the length of the rectangle is:"))
breadth=int(input("the breadth of the rectangle is:"))
area=length*breadth
print (area )
# >>> length=int(input("the length of the rectangle is:"))
# the length of the rectangle is:20
# >>> breadth=int(input("the breadth of the rectangle is:"))
# the breadth of the rectangle is:30
# >>> area=length*breadth
# >>> print (area )
# 600
# >>> the code works well if you run it line by line as the first variable gets the values assigned then and then the second variable gets it and finally when you ask 
# the print command to print  the result then it fetches the values and prints that



# the reason why python was showing error because python uses an interpreter and so if you run the full code then what happens is that the python shows error as 
# as the variables declared had no values in them
# then the next question is thet what is the function of int in the main equation 
# to demonstrate that lets run the code without int and what i think will eventually happen is that the python will just join the two numbers and not add them



length=(input("the length of the rectangle is:"))
breadth=(input("the breadth of the rectangle is:"))
area=length*breadth
print (area )

# >>> length=(input("the length of the rectangle is:"))
# the length of the rectangle is:20
# >>> breadth=(input("the breadth of the rectangle is:"))
# the breadth of the rectangle is:50
# >>> print (area )
# 600
# >>>

# note that the answer is 600 which might be because of the previous variables and also because 20x50=1000