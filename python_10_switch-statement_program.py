
a = int(input("Enter a number between 1-10 :"))
match a:
    case 1:
        print("You chose One")
    case 2:
        print("You chose Two")
    case 3:
        print("You chose Three")
    case 4:
        print("You chose Four")
    case 5:
        print("You chose Five")
    case 6:
        print("You chose Six")
    case 7:
        print("You chose Seven")
    case 8:
        print("You chose Eight")
    case 9:
        print("You chose Nine")
    case 10:
        print("You chose Ten")
    case _:                                                 #Underscor "_" for default option This is also known as (else) in other language
        print("Sorry You chose More Than Ten")



#Another Example of Switch System

b = int(input("Enter a Nimber: "))
match b:
    case 5:
        print("Your choice is 5")
    case _ if (b!=90):
        print("You Lose me")
    case _ if (b != 13):
        print("Your chose is best")
