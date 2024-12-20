# LIST mutable in python
# it hold multiple data type at a time

info = [23,'vishal',67,"Delhi"];
print(info);
print(info[1]);
info[1] = 'yadav'; # mutable in py
print(info[1]);
print(type(info));
print(len(info));

# SLICING is here
print(info[1:]); # end tak
print(info[-3:]); # end tak

# LIST METHOD
info.append('5');
print(info);
mark = [5,4,6,2,5,2,3]
mark.sort() # the only works on same data type value in list
print(mark) # incresing order
mark.sort(reverse=True) # the only works on same data type value in list
print(mark) # decreasing order
info.reverse()
print(info);
info.insert(len(info)-1,"k");
print(info);

# Check Docs further methods
