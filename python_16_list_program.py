#List

list=[2,5,6,7,11,8,34,23,21,48,50,58,45,80,76]
print(list)                 #Output -    [2, 5, 6, 7, 11, 8, 34, 23, 21, 48, 50, 58, 45, 80, 76]
print(type(list))           #Output -    <class 'list'>
print(list[0])              #Output -     2
print(list[1])              #Output -     5
print(list[2])              #Output -     6
print(list[3])              #Output -     7
print(list[4])              #Output -     11
print(list[5])              #Output -     8
print(list[6])              #Output -     34
print(list[7])              #Output -     23
print(list[8])              #Output -     21
print(list[9])              #Output -     48
print(list[10])             #Output -     50
print(list[11])             #Output -     58
print(list[12])             #Output -     45
print(list[13])             #Output -     80
print(list[14])             #Output -     76

#Negative index

print(list[-3])             #Output -     45
print(list[len(list)-3])    #Output -     45
print(list[15-3])           #Output -     45
print(list[12])             #Output -     45     (P0setive index)

#Cheak the Item

if 21 in list:
    print("Yes")
else:                       #Output -     Yes
    print("No")

if 78 in list:
    print("Yes")
else:                       #Output -     No
    print("No")

#Jump Index

print(list[1:10])           #Output -      [5, 6, 7, 11, 8, 34, 23, 21, 48]
print(list[6:1])            #Output -      []
print(list[5:-6])           #Output -      [8, 34, 23, 21]
print(list[-10:4])          #Output -      []
print(list[10:6])           #Output -      []
print(list[-1:10])          #Output -      []
print(list[:9])             #Output -      [2, 5, 6, 7, 11, 8, 34, 23, 21]
print(list[9:])             #Output -      [48, 50, 58, 45, 80, 76]
print(list[-1:])            #Output -      [76]
print(list[:-10])           #Output -      [2, 5, 6, 7, 11]


print(list[1:12:6])         #Output -      [5, 23]
print(list[1:11:2])         #Output -      [5, 7, 8, 23, 48]
print(list[4:12:3])         #Output -      [11, 23, 50]
print(list[6:12:1])         #Output -      [34, 23, 21, 48, 50, 58]
print(list[1:10:3])         #Output -      [5, 11, 23]
print(list[1:12:5])         #Output -      [5, 34, 58]


lst = [l*l for l in range(5)]
print(lst)                  #Output -      [0, 1, 4, 9, 16]
lst = [l for l in range(5)]
print(lst)                  #Output -      [0, 1, 2, 3, 4]
