#Default argument

def averagename(fname, mname = "ranjan" ,lname= "Mallick"):
    print("Hello,",fname, mname, lname)
averagename("Smruti")

#output
"""
Hello, Smruti ranjan Mallick
"""

#Keyword argument

def king(fname, mname, lname):
    print("Hello,",fname, mname, lname)
king(mname = "Jack" , lname = "Sparow" , fname="Capten")

#Output
"""
Hello, Capten Jack Sparow
"""

#Required arguments

def name(fname, mname, lname):
    print("Hello,",fname, mname, lname)
name("Rusty", "Nails")

#Output
"""
    name("Rusty", "Nails")
TypeError: name() missing 1 required positional argument: 'lname'
"""

#Keyword Arbitrary Arguments

def Smruti(**Smruti):
    print("Hello,", Smruti["fname"], Smruti["mname"], Smruti["lname"])
Smruti(mname = "Love", lname = "you",fname = "I" )

#Output
"""
Hello, I Love you
"""

#Return Statement

def love(fname, mname, lname):
    return "Hiii..." + fname + " " + mname + " " + lname
print(love("I","Am","Smrutiranjan"))

#Output
"""
Hiii...I Am Smrutiranjan
"""
