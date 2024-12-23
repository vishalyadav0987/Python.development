# mutable
# not allow dupplicated key
# not allow empty key
# not allow empty value
# It store data in the form key:value pair
# unorderd


dict = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "subjects":["math","sicence"],
    "marks": (89,98),
    "is_online": True,
    "is_admin": False,
    23.5:45,
    45:"hello"
}

print(dict);
print(type(dict));
print(dict["name"]);
print(type(dict["age"]));
dict["name"] = "vishal"; # update overtire previos key
print(dict);
dict["age"] = 30; # update overtire previos key

# Add key:value to dict
dict["country"]="india";
print(dict);

# print(dict["hero"]); # in the case give error keyError


# NULL dict
Null_dict = {};
print(Null_dict);

# Addd
Null_dict["name"]="vishal";
print(Null_dict);


# Nested Dictionary in Python
nested_dict = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "subjects": {
        "math": 90,
        "science": 85,
        "english": 88
    },
    "marks": (89,98),
    "is_online": True,
}

print(nested_dict);

print (nested_dict["subjects"]["math"]);

nested_dict["subjects"]["math"] = 95;
# add
nested_dict["subjects"]["history"] = 90;
print(nested_dict);

# print(nested_dict.keys()); # return all keys
# if we in array form
print(list(nested_dict.keys()))
# print(nested_dict.values()); # return all values
# if we in array form
print(list(nested_dict.values()))
# print(nested_dict.items()); # return all key-value pairs
print(list(nested_dict.items()))
print(list(nested_dict.items())[0])
print(nested_dict.get("name")); # return value of key if key not exsist the simply return none
print(nested_dict.get("name","default")); # return value of key if key exist otherwise return

newDict = {
    "ok":"why",
}
nested_dict.update(newDict); # insert new dict to old dict
print(nested_dict);

print(len(nested_dict)); # return number of key-value pairs