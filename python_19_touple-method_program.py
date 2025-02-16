tuple1 = (1, 2, 5, 4, 5, 2, 1, 7, 9, 4, 5, 6, 7, 1, 2, 2, 6)
res = tuple1.count(2)             #Output - 17
res = tuple1.index(5)             #Output - 2
res = tuple1.index(2, 4, 9)       #Output - 5  """2 is element 4 to 9 is range"""
res = len(tuple1)
print(res)
