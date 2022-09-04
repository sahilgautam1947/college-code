# •• All taxpayers are charged a flat tax rate of 20% 
# •• All taxpayers are allowed a $10,000 standard deduction.
# •• For each dependent, a taxpayer is allowed an additional $3,000 deduction. 
# •• Gross income must be entered to the nearest penny.
# •• The income tax is expressed as a decimal number








# the constants
taxrate=.20
standarddeduction=10000.0
dependentdeduction=3000.0

# request for inputs
grossincome= float(input("enter the gross income:"))
numdependents=int(input("enter the number of dependents:"))
# compute the income tax
taxableincome=grossincome-(standarddeduction + numdependents*dependentdeduction) 
incometax=taxableincome*taxrate

print("this is the tax in dollars:",incometax)

# this is working
