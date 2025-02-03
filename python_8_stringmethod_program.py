a="Smrutiranjan"
print(len(a))       #12
print(a)            #Smrutiranjan
print(a.upper())    #SMRUTIRANJAN
print(a.lower())    #smrutiranjan


b="!!!Smruti!!!!!!!! !!!!!!Smruti!!!!!!!!!  Smruti!!!!  Smruti!!!!!"
print(b.rstrip("!"))                 #!!!Smruti!!!!!!!! !!!!!!Smruti!!!!!!!!!  Smruti!!!!  Smruti
print(b.replace("Smruti","Nikhil"))  #!!!Nikhil!!!!!!!! !!!!!!Nikhil!!!!!!!!!  Nikhil!!!!  Nikhil!!!!!
print(b.split(" "))                  #['!!!Smruti!!!!!!!!', '!!!!!!Smruti!!!!!!!!!', '', 'Smruti!!!!', '', 'Smruti!!!!!']
print(b.count("Smruti"))             #4
print(b.endswith("!!!!"))            #True
print(b.endswith("to",4,10))         #False


fartune="it Is a Institute in this institute we study about Computer"
print(fartune.capitalize())          #It is a institute in this institute we study about computer


tricks="Welcome to Tricks !!!!"
print(len(tricks))                   #22
print(len(tricks.center(50)))        #50


Hello="I am Rohan from India and I'm from India and also I love my contry more than any thing."
print(Hello.find("am"))              #2
print(Hello.index("am"))             #2
print(Hello.isalnum())               #False


x="Welcome"
print(x.isalpha())                   #True
print(x.islower())                   #false


y="We all are friends. \n so dont fight together"
print(y.isprintable())              #false
