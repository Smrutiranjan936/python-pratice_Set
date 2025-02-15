i = [10, 58, 61, 51, 20, 45, 63, 58, 45, 58, 16, 11, 2, 45]
i.append(63)                #Output - [10, 58, 61, 51, 20, 45, 63, 58, 45, 58, 16, 11, 2, 45]               """This function used to add a new element in the end of list"""
i.sort()                    #Output - [2, 10, 11, 16, 20, 45, 45, 45, 51, 58, 58, 58, 61, 63, 63]           """This function used to arrange the element to ascending order"""
i.sort(reverse=True)        #Output - [63, 63, 61, 58, 58, 58, 51, 45, 45, 45, 20, 16, 11, 10, 2]           """This function used to arrange the element to descending order"""
i.reverse()                 #Output - [63, 45, 2, 11, 16, 58, 45, 58, 63, 45, 20, 51, 61, 58, 10]           """This function used to arrange the element to reverce order"""
print(i.index(58))          #Output - 1        """This function used to find the index of the element"""
print(i.count(58))          #Output - 3        """This function used to how many time the element is use in the list"""
i.insert(3, 80)             #Output - [10, 58, 61, 80, 51, 20, 45, 63, 58, 45, 58, 16, 11, 2, 45]           """In this function we can add the new element in the given index"""
m = i
m[0] = 0                    #Output - [0, 58, 61, 51, 20, 45, 63, 58, 45, 58, 16, 11, 2, 45]                """Replace the index of given element"""
m = i
m[1] = 5                    #Output - [10, 5, 61, 51, 20, 45, 63, 58, 45, 58, 16, 11, 2, 45]                """Replace the index of given element"""
m = [100, 200, 300]
i.extend(m)                 #Output - [10, 58, 61, 51, 20, 45, 63, 58, 45, 58, 16, 11, 2, 45, 100, 200, 300]"""Murtz the two list"""
print(i)
s = [55,65,75]
a = [50,60,70]
sa =s+a
print(sa)                   #Output - [55, 65, 75, 50, 60, 70]          """Murtz the two list"""
