#Lab. work 2-1 (variables)

#Create any variable with name var1
var1 = 'villahermosa'

#Check type of var1 with type function
print("var1 {} is of {}".format(var1, type(var1)))

#Check is var1 is True
print("var1 {} is True: {}".format(var1, bool(var1)))

#Check is var1 is False
print("var1 {} is False: {}".format(var1, not bool(var1)))

#Create var2 that equal to (var1 or True)
var2 = var1

#Check is var2 is True
print("var2 {} is True: {}".format(var2, bool(var2)))

#Check is var2 is False
print("var2 {} is False: {}".format(var2, not bool(var2)))

#Check result for var2 and var1
print("var2 {} the result is: {}".format(var2, bool(var1)))