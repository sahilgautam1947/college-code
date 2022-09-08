# the software developement process is a lot more than just programming as 
# it takes a lot to write a good code 

# first of all the need for programming is analysed that may be customer project or some other requirement 
# the next thing that is done is to analyse what the programm will do 
# the next step is design that is how the programm will do the task required 
# then comes the coding step in which the code is written 
# then it is the integration part in which we combine the smaller parts to make a smoothly working programm which is not easy 
# and the most important part is maintainence which is usually the most expensive one 


# sometinmtimes bugs are found in the programm so as to solve them we may have to go to the previous steps also 



# Q List four phases of the software development process, and explain what they accomplish

# ans 

#     requirement 
#     what the programm will do 
#     how the programm will do 
#     coding part 
#     integration 
#     implimentation
#     maintainence 


# Q Jack says that he will not bother with analysis and design but proceed directly to coding his programs.
#  Why is that not a good idea?

#  ans 

#      this is not a good idea as to write a good code it is the basic requirement that thorough analysis is done 
#      so as to prevent bugs or unstabilirty issues in later stages 
#      also if some thing like a blue print or a pseudocode is made in advanced then it then becomes really easy 
#      to code when the logic has been previously build and the planning has been done 

# new shotcut discovered 
# if you press ctrl+shift plus any arrow keys then a word gets selected and 
# that combination of words is highlighted in the whole code 





length=(input("the length of the rectangle is:"))
breadth=(input("the breadth of the rectangle is:"))
area=length*breadth
print (area )

# >>> length=(input("the length of the rectangle is:"))
# the length of the rectangle is:200
# >>> breadth=(input("the breadth of the rectangle is:"))
# the breadth of the rectangle is:300
# >>> area=length*breadth
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can't multiply sequence by non-int of type 'str'
# >>> print (area )
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'area' is not defined
# >>>


# vs




length=int(input("the length of the rectangle is:"))
breadth=int(input("the breadth of the rectangle is:"))
area=length*breadth
print (area )

# >>> length=int(input("the length of the rectangle is:"))
# the length of the rectangle is:25
# >>> breadth=int(input("the breadth of the rectangle is:"))
# the breadth of the rectangle is:50
# >>> area=length*breadth
# >>> print (area )
# 1250
# >>>




length=int(input("the length of the rectangle is:"))
breadth=int(input("the breadth of the rectangle is:"))
area=length*breadth
print (area )

# >>> length=int(input("the length of the rectangle is:"))
# the length of the rectangle is:asdf
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: 'asdf'
# >>>

# this is what happens when you enter wrong data type for other


length=(input("the length of the rectangle is:"))
breadth=(input("the breadth of the rectangle is:"))
area=length+breadth
print (area )
# if you dont tell the data type then by default it takes string or considers as string and it shows error in case of nultuplication as it is not defined for strings

# >>> length=(input("the length of the rectangle is:"))
# the length of the rectangle is:50
# >>> breadth=(input("the breadth of the rectangle is:"))
# the breadth of the rectangle is:50
# >>> area=length+breadth
# >>> print (area )
# 5050
# >>>
#  here it has kind of joined the inputs 


# also subtraction and multiplication and division should not be valid 

length=(input("the length of the rectangle is:"))
breadth=(input("the breadth of the rectangle is:"))
area=length-breadth
print (area )



# >>> length=(input("the length of the rectangle is:"))
# the length of the rectangle is:1200
# >>> breadth=(input("the breadth of the rectangle is:"))
# the breadth of the rectangle is:5050
# >>> area=length-breadth
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for -: 'str' and 'str'
# >>> print (area )
# 5050                so it might have printed the area from the previous result
# >>>















length=(input("the length of the rectangle is:"))
breadth=(input("the breadth of the rectangle is:"))
area=length+breadth
print (area )

# >>> length=(input("the length of the rectangle is:"))
# the length of the rectangle is:asdf 
# >>> breadth=(input("the breadth of the rectangle is:"))
# the breadth of the rectangle is:jkl; 
# >>> area=length+breadth
# >>> print (area )
# asdf jkl;
# >>>





# so the conclusion about the input function is that it by default takes strings and if not mentioned float or int then it takes the characters of the int and 
# the float as strings and that is all demonstrated above
