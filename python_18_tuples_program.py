rock = (1, 2, 3, 5, 8, 9)           #Output - tuple need atlist one comma (,)
print(type(rock), rock)             #Output - <class 'tuple'> (1, 2, 3, 5, 8, 9)
# rock[0] = 90                        #Output - TypeError: 'tuple' object does not support item assignment
print(len(rock))                    #Output - 6
print(rock[0])                      #Output - 1
print(rock[1])                      #Output - 2
print(rock[2])                      #Output - 3
print(rock[3])                      #Output - 5
print(rock[4])                      #Output - 8
print(rock[5])                      #Output - 9
print(rock[-5])                     #Output - 2
print(rock[-2])                     #Output - 8
#Condition check
if 6 in rock:
    print("Yes it's present")       #Output - No it's not present
else:
    print("No it's not present")
#Slicing
rockey = rock[2:5]
print(rockey)                       #Output - (3, 5, 8)


"""tuples are immutable ordered collections of elements, similar to lists but with the key difference that tuples cannot be modified after their creation"""
