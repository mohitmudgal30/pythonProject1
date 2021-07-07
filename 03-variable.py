var1 ="this is a string"
var2 =4
var3 =36.7
var4 =" mohit mudgal"
var5 ="20"
var6 ="5.5"
print(type(var1))
print(type(var2))
print(type(var3))
print("the sum is", var2+var3)
print(var2+var3)
print(var1+var4)

#by typecasting we can change string to a int or a float
"""
typecasting
int()
str()
float()
"""
print(int(var5)+float(var6))

print(5*"hello world\n")
print(var4*5)
print(10*str(var2+var3))

print("Enter a number")
inpnumber =input() # input() behave as a string
print("you entered",inpnumber)
print("you added =",int(inpnumber)+10)

#sum of two no.  by taking input
print("enter first no.")
n1 =input()
print("enter second no.")
n2 =input()
print("the sum of n1 and n2 is",int(n1)+int(n2) )
