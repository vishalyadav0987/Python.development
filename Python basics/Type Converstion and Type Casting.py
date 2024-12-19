# TYPE CONVERSTION : when computer automatically handle the datatype int to float or vice versa
a = 2
b = 4.5

sum = a+b # 2.0 + 4.5 => 6.5
print(sum);

# but one value is string type
c = "2"
d = 4.5

# in the type converstion isn't possible
# so we Use

# TYPE CASTING : It is methond to do manually casting float to int to string to int vice versa

e = 4
f =5.6
g = "4"

sum2 = (e) + int(f) + int(g)
sum3 = float(e) + (f) + float(g)
print(sum2," ",sum3);

h = 4;
h = str(h);
print(type(h));

