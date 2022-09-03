# # # print(<expression>) 
# # # it is a command used to print any thing in python_branch

# # #  In Python code, a string is always enclosed in quotation marks. However, the print function displays a string without
# # # the quotation marks.

# # from pdb import line_prefix


# # You can also write a print function that includes two or more expressions separated by commas

# # The syntax for a print statement with two or more expressions looks like the following:
# # print(<expression>,..., <expression>)

# # Note the ellipsis (...) in this syntax example. The ellipsis indicates that you could include multiple expressions after the first one. 

# # Whether it outputs one or multiple expressions, the print function always ends its output with a newline
# # this means that the curser at the end of the programm would end up in a new line or the next line 


# # To begin the next output on the same line as the previous one, you can place the expression end = "", which says “end the line with an empty string instead of a newline,” at the end of the list of expressions, as follows:
# # print(<expression>, end = "")


# name = input("Enter your name: ")   
# # here the input is a function that takes an input and to take that input it shows the prompt which is written in the input function  
# # then on the left you assign the variable in which you want to store the return value and thats it you got the input and stored it

# # >>> name = input("Enter your name: ")   
# # Enter your name: 22265
# # >>> name
# # '22265'
# # >>> print(name) 
# # 22265
# # >>>


# name = input(55)   
# # this also works
# # >>> name = input(55)   
# # 55sahil
# # >>> name
# # 'sahil'
# # >>> print(name) 
# # sahil
# # >>>

# name = input(  )   
# # this also works
# # >>> name = input(  )
# # sahil
# # >>> print(name)
# # sahil
# name = input()
# # and this also works
# # >>> name = input()
# # sahil
# # >>> print(name)
# # sahil

# name = input("Enter your name: ")   
# # >>> name = input("Enter your name: ")   
# # Enter your name: sahil
# # >>> name
# # 'sahil'
# # >>>

# # if you declared a string as a variable then you need not use"" as it is a variable 



# # i want this programm to run 
# # a=input("length of rectangle") 
# # b=20
# # p= a*b



# # whats wrong with this code 
# # a=464466
# # b=input("second number")
# # print(a+b)

# length=int(input("the length of the rectangle is:"))
# breadth=int(input("the breadth of the rectangle is:"))
# area=length*breadth
# print (area )
# # >>> length=int(input("the length of the rectangle is:"))
# # the length of the rectangle is:20
# # >>> breadth=int(input("the breadth of the rectangle is:"))
# # the breadth of the rectangle is:30
# # >>> area=length*breadth
# # >>> print (area )
# # 600
# # >>> the code works well if you run it line by line as the first variable gets the values assigned then and then the second variable gets it and finally when you ask 
# # the print command to print  the result then it fetches the values and prints that




# #looks like the last time it was human error and may be i was executing wrong way like just running the print area but then if new
# # values  are assigned to the length and breadth then why only running print area prints the older result
# >>> length=int(input("the length of the rectangle is:"))
# the length of the rectangle is:2000000
# >>> breadth=int(input("the breadth of the rectangle is:"))
# the breadth of the rectangle is:2000000
# >>> area=length*breadth
# >>> print (area )
# 4000000000000
# >>> print (area )
# 4000000000000
# >>> print (area )
# 4000000000000
# >>> length=int(input("the length of the rectangle is:"))
# the length of the rectangle is:1000000000000
# >>> breadth=int(input("the breadth of the rectangle is:"))
# the breadth of the rectangle is:100000000000
# >>> print (area )
# 4000000000000
# >>> area=length*breadth
# >>> print (area )
# 100000000000000000000000
# # 
# # 
# # but when i try to run it again with different values of variables

# >>> length=int(input("the length of the rectangle is:"))
# the length of the rectangle is:50000
# >>> breadth=int(input("the breadth of the rectangle is:"))
# the breadth of the rectangle is:20000
# >>> print (area )
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'area' is not defined
# >>> area=length*breadth
# >>> print (area )
# 1000000000
# >>> length=int(input("the length of the rectangle is:"))
# the length of the rectangle is:10000
# >>> breadth=int(input("the breadth of the rectangle is:"))
# the breadth of the rectangle is:50000
# >>> print (area )
# 1000000000
# >>>
# # this is the wiered kind of behaviour i was struggeling with 
# # at first it works fine but later it prints out the same result as the previous one but why?
# # is it because the containers named length and breadth are already full and will not change if i re run the code in the terminal and provide new values there 
# # does it require me to either use new names for the variables or 

# # and one more thing onced assigned the variables till how long do they hold to their assigned values and how to clear them for new set of values












# # the reason why python was showing error because python uses an interpreter and so if you run the full code then what happens is that the python shows error as 
# # as the variables declared had no values in them
# # then the next question is thet what is the function of int in the main equation 
# # to demonstrate that lets run the code without int and what i think will eventually happen is that the python will just join the two numbers and not add them



# length=(input("the length of the rectangle is:"))
# breadth=(input("the breadth of the rectangle is:"))
# area=length*breadth
# print (area )

# # >>> length=(input("the length of the rectangle is:"))
# # the length of the rectangle is:20
# # >>> breadth=(input("the breadth of the rectangle is:"))
# # the breadth of the rectangle is:50
# # >>> print (area )
# # 600
# # >>>

# # note that the answer is 600 which might be because of the previous variables and also because 20x50=1000





# # Programmers inevitably make typographical errors when editing programs, and the Python interpreter will nearly always detect them.
# # Such errors are called syntax errors. The term syntax refers to the rules for forming sentences in a language. When Python encounters a syntax error in a program, it halts execution with an error message.
# # The following sessions with the Python shell show several types of syntax errors and the corresponding error messages:
# # >>> length = int(input("Enter the length: "))
# # Enter the length: 44
# #  >>> print(lenth)
# # Traceback (most recent call last): File "<pyshell#l>", line 1, in <module> NameError: name 'lenth' is not defined

# # The first statement assigns an input value to the variable length. The next statement attempts to print the value of the variable lenth. Python responds that this name is not defined. Although the programmer might have meant to write the variable length,
# # Python can read only what the programmer actually entered. This is a good example of the rule that a computer can read only the instructions it receives, not the instructions we intend to give it.
# # The next statement attempts to print the value of the correctly spelled variable. However, Python still generates an error message.

# # >>> print(length) SyntaxError: unexpected indent

# # In this error message, Python explains that this line of code is unexpectedly indented.
# # In fact, there is an extra space before the word print. Indentation is significant in Python code. Each line of code entered at a shell prompt or in a script must begin in the leftmost column,
# # with no leading spaces. The only exception to this rule occurs in control statements and definitions, where nested statements must be indented one or
# # more spaces



# # Q1.   Suppose your script attempts to print the value of a variable that has not yet been assigned a value. How does the Python interpreter react?
# name=input("waht is your name :  ")
# print(name)
# #    >>> name=input("waht is your name :  ")
# #    waht is your name :  print(name)
# #  this is what happens when you run the whole code at once






# # Q2.   Miranda has forgotten to complete an arithmetic expression before the end of a line of code. How will the Python interpreter react?

# 3+3
# # >>> 3+3
# # 6
# # >>>

# 3+
# # >>> 3+
# #   File "<stdin>", line 1
# #     3+
# #       ^
# # SyntaxError: invalid syntax
# # >>>


# # Q3.   Why does Python code generate fewer types of syntax errors than code in other programming languages?
# # because this is newer language and it has automated many steps like identifying the type of the integer so at last less errors as compared to other languages





