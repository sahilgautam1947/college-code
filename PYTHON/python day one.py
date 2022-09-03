# 00    remember that variable cannot be declared when it starts with a string eg 132asdf
# types of errors of variable declaration
# 01    you cannot use anysymbol except for underscore _  sahil_123
# sahil)+ 213 is a wrong variable
# 02    already defined functions cannot be declared as variables 
# eg  class = 20 is technically wrong
 


var=10
print(var)
# shift plus enter to run selection
# DATA TYPES---- INTEGERS AND STRINGS AND VARIABLES

a=10
type(a)
#>>> a=10 >>>---- type(a)----- <class 'int'>
b=10
type(b)
# >>> b=10 ---->>> type(b)----<class 'int'>
# python is a case seneitive language
# = is the assignment operator
a=10
b=20
# a,b= 10,20 can also be used to assign variables in one line
# write a program to swap the two numbers
#a,b = b,a concept of temperary container (elaborate later. )
#  ##
a=10
b=20
temp=a
a=b
b=temp
print(a)
print(b)

#import keyword
#keyword.iskeyword("class") this is tocheck whether class is a keyword
# operator(+,-,* ,** ,% ,/ float division it gives answer with a decimal ,// it is integer division and it gives the gint of the answer,=,==) and operands
# a+b=c here a,b,c are operands and + and = are operators
#  # 
# ##
a=10
b=20
a,b=b,a
print (a)
print(b)
#   >>> a=10------>>> b=20----->>> a,b=b,a---->>> print (a)----20----->>> print(b)----10

a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(2**10)
print(4%2)# this will return remainder
# two types of divisions integer devision and float divisiion
print("float division", 4/2)#this is float division as it gives answer as an integer eg 2.0
print("float division", 4.0/2)
print("float division", 4/2.0)# here the text is just a string attached and does not have anything to do with the division type

print("integer division", 4//2)#int dividion also considers the concept of significant figures so if you write 2.0//2 your answer eill be 1.0 as per the rule that the lowest significant figure is considersd
print("integer division", 4.0//2)
print("integer division", 4//2.0)


#if there are more than one operators in a single line then the following is the order of preferences
# 01
# 02
# 03
# 04
# 
# ##


# operators on strings
a="fun"
b="class"
print(a+b)# here it is not adding but joining the strings this is  called concatination

"fun"*3
#>>> "fun"*3 'funfunfun'

'fun'*3
#>>> "fun"*3 'funfunfun'
b="fun"
print(b*3)

# there are 29 keywords in python
# and (logical and) from boolean algebra
# assert( used for debugging purposes)
# break to stop
# class to define class
# 
# 
#bodmass for python
#########
