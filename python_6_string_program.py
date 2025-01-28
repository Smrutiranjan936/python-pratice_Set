a="Smrutiranjan";
b="Rohan";
c='Kalia';
d='Suvendu';
print("hello,"+a);
print("hello,"+b);
print("hello,"+c);
print("hello,"+d);

e="Hello bro,"i am here"
print(e);     # give error because doblecot is used in middle

e="Hello bro,\"i am here"
print(e);    #now it not give error



"""Multyline string"""

f="Hii ram,
How are you,
What u do"
print(f);  #give error

f='''Hii ram,
How are you,
What u do'''
printf(f); #now it run

"""Index"""

g="abcde";
print(g[0]);    #Ans-a
print(g[1]);    #Ans-b
print(g[2]);    #Ans-c
print(g[3]);    #Ans-d
print(g[4]);    #Ans-e
print(g[5]);    #Ans-Error


"""For loop whit String"""

for character in g:
  print(character)

