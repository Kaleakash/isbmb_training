num1=[56,78,24,90,78];
stdNames=["Raj","Ravi","Ramesh","Lokesh","Ajay"];
print(num1);
print(stdNames);
print("first number ",num1[0]);
print("second name ",stdNames[1]);
names=[];       # empty list created 
names.append("Ajay");       # add the names in list 
names.append("Lokesh");
names.append("Vikash");
print(names);
names.pop();            # remove the name from list
print(names);
names.remove("Ajay");   # remove using value 
print(names);
