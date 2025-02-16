letter = "Hii, My name is{} and I am from{}"
country = "India"
name = "Smrutiranjan"
print(letter.format(name,country))                              #Output - Hii, My name isSmrutiranjan and I am fromIndia
#OR
print(f"Hii, My name is {name} and I am from {country}")        #Output - Hii, My name isSmrutiranjan and I am fromIndia
#OR
letter = "Hii, My name is{0} and I am from{1}"
print(letter.format(name,country))                              #Output - Hii, My name isSmrutiranjan and I am fromIndia



txt = "For only {price:.2f} dollars!"
print(txt.format(price = 59.0912))                              #Output - For only 59.09 dollars!
#OR
price=29.0954
test = f"For only {price:.2f} dollars!"
print(test)                                                     #Output - For only 29.10 dollars!


print(f"{2*50}")                                                #Output - 100
print(type(f"{2*50}"))                                          #Output - <class 'str'>

print(f"Hii, My name is {{name}} and I am from {{country}}")    #Output - Hii, My name is {name} and I am from {country}

