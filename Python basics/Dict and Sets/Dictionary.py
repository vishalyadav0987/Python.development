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


# NULL dict
Null_dict = {};
print(Null_dict);

# Addd
Null_dict["name"]="vishal";
print(Null_dict);