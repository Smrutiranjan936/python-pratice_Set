a=int(input("Enter your age :"));
if(a>18):
    print("You can drive");        #the space is called "Indentation"
else:
    print("you cant drive");


#condition Operators
# (  >,<,>=,<=,==,!=  )


print(a>18);            #False
print(a<18);            #False
print(a>=18);           #True
print(a<=18);           #True
print(a==18);           #True
print(a!=18);           #False


#if-else statement


ApplePrice = 160;
budget = 150;
if(ApplePrice <= budget):
    print("I can buy the Apple")
else:
    print("I can't buy the Apple")


#if-elseif


ApplePrice = int(input("Enter the ApplePrice:"))
budget = int(input("Enter Your budget:"))
if(budget - ApplePrice > 40):
    print("I want to buy 1kg Apple")
elif(budget - ApplePrice > 80):
    print("I want to buy 50g Apple")
else:
    print("I don't want to buy Apple")


#nested if statement


num = int(input("Enter a number:"))
if(num < 0):
    print("Number is negative.")
elif(num > 0):
    if( num <= 10):
        print("Number is between 1-10")
    elif( num > 10 and num <=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Zero");


