# immutable
# unorderd
# unindexed
# unchangeable
# All value are unquie
# list and dict can not store in set because both are mutable

set1 =  {1, 2, 3, 4, 5,"hello","world","hello",5} 
print(set1);
print(type(set1));

empty_set = {} # empty dictionary
print(type(empty_set));

empty_set = set() # empty set
print(type(empty_set));


set1.add(0);
print(set1)
set1.remove(5);
print(set1)
set1.pop() # remove random value
print(set1)
set1.clear() # remove all value
print(set1)

# NOTE : set is mutable but element of set is immutable

set3 = {
    1,
    2,
    3,
    (1,2,3,4),
    "vishal",
}

set3.add((6,7,8,9));
# set3.add([1,2,3,4,5,6,7,8]);
# this will throw error because list is mutable also it hassable value alway change if new value enter in a list

print(set3);



set4 = {1,2,3,45};
set5 = {1,2,3,4};
set5.union(set4); # return new set
print("union",set4);

print("intersection",set4.intersection(set5)) # return new set