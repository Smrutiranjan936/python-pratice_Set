#for loop for string
name = 'smruti';
for i in name:
    print(i)

#Output
"""
s
m
r
u
t
i

"""

#nested for loop

a = 'smrutiranjan';
for j in a:
   print(j)
   if(j=="a"):
       print("special char")


#Output
"""
s
m
r
u
t
i
r
a
special char
n
j
a
special char
n

"""

#nested for loop

colors = ["Blue","Black","White","Red","Yellow","gray"]
for color in colors:
    print(color);
    for m in color:
        print(m)
#output
"""
Blue
B
l
u
e
Black
B
l
a
c
k
White
W
h
i
t
e
Red
R
e
d
Yellow
Y
e
l
l
o
w
gray
g
r
a
y
"""

#range function

for l in range(10):
    print(l);

#output
"""
0
1
2
3
4
5
6
7
8
9
"""

for t in range(10, 21):
    print(t)

#output
"""
10
11
12
13
14
15
16
17
18
19
20

"""

for f in range(5, 95, 10):
    print(f)

#output
"""
5
15
25
35
45
55
65
75
85

"""

for d in range(5):
    print(d+1)

#output
"""
1
2
3
4
5

"""
