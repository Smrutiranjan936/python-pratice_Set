#Basic type

a = 50
b = 30
if(a>b):
    print("first number is greater")
else:
    print("Second number is greater")
question1 = (a+b)/(a-b)
print(question1)
c = 20
d = 60
if(c>d):
    print("first number is greater")
else:
    print("Second number is greater")
question2 = (c+d)/(c-d)
print(question2)


#Same type but in function method

def calculate(a, b):
    question = (a+b)/(a-b)
    print(question)
a = 50
b = 30
if(a>b):
    print("first number is greater")
else:
    print("Second number is greater")
calculate(a, b)
c = 20
d = 60
if(c>d):
    print("first number is greater")
else:
    print("Second number is greater")
calculate(c, d)

#Another in better way

def calculate(a, b):
    question = (a+b)/(a-b)
    print(question)
def cheaking(a, b):
    if (a > b):
        print("first number is greater")
    else:
        print("Second number is greater")
def nothing(a, b):          #this pass statement can alow to exicute the code
    pass                    #Pass besically used when the developer can forget something when he writing the cade . the pss statement can allow to exicute the code without giving error
a = 50
b = 30
calculate(a, b)
cheaking(a, b)
c = 20
d = 60
calculate(c, d)
cheaking(c, d)




#Output

"""
first number is greater
4.0
Second number is greater
-2.0
"""
