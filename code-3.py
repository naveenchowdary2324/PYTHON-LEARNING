#DataTypes

#NumericDataTypes
num1 = 10 #integer
num2 = 10.02 #Float
num3 = 10j #Complex
print(num1,type(num1))
print(num2,type(num2))
print(num3,type(num3))

#SequentialDataTypes

Str1 = "this is a string" #String
print(Str1,type(Str1))

list1 = [1,2,3,4,5,6] #Lists
print(list1,type(list1))
print(list1[0])

Tuple1 = (1,2,3,4,5,6) #Tuple
print(Tuple1,type(Tuple1))
print(Tuple1[0])

#Dictionary
dict1 = {
    "name" : "Naveen",
    "age" : 22,
    "skill": "Python"
}
print(dict1,type(dict1))
print(dict1["name"])

#set

set1 = {1,2,3,4,5,6}
print(set1,type(set1))
