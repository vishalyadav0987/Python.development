# concatenation
a = "vishal";
b = 'yadav';
c = '''this is multiline string
this is second line'''; # this cotetion of multiline string


print("a + b =>", a+b);
print(len(b)); # len of string
print(c);

# print using index
print(a[4]); 

# string in pyhton is unmutable
# a[4] = "f";
# print(a[4]); 

# SLICING
print(a[1:4]); # 1,2,3 tak idx
print(a[1:]); # ending tak
print(a[:4]); # start se
print(a[:len(a)]); # end tak


# String also have BACKWORD INDEXING starts -1
print(a[-5:-2]); # 1,2,3 tak idx

print(c.endswith("line"));
print(c.capitalize());
print(c.find("this")); # always find 1st occurenece # return index
print(c.replace("this","that")) # not affect original string is immmutable in py [chage all occ]
print(c.count("this"));



# CONDITIONAL IS DONE (if else elif)


