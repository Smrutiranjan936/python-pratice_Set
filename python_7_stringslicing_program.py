name = "Smrutiranjan"
len1 = len(name);
print("length is a",len1,"Letter word.")

#output - length is a 12 Letter word.


"""Slicing"""

print(name[0:12]);    #output - Smrutiranjan
print(name[:8]);      #output - Smrutira
print(name[:]);       #output - Smrutiranjan
print(name[8:]);      #output - njan
print(name[5:10]);    #output - iranj

'''both are same'''
print(name[-1:12]);
print(name[len(name)-1:12]);                #output - n
print(name[11:12]);

'''both are same'''
print(name[-10:-4]);
print(name[len(name)-10:len(name)-4]);      #output - rutira
print(name[2:8]);

'''both are same'''
print(name[6:-5]);
print(name[6:len(name)-5])                  #output - r
print(name[6:7]);
