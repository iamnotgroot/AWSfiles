print("Phyton has three numeric types: int, float, and complex")

myValue=1
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the date type " + str(type(myValue)))

myValue=3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

"""Week 5 Day 3"""
"""Define a List"""
myFruitList = ["apple", "banana","cherry"]
print(myFruitList)
print(type(myFruitList))

"""Access list by position"""
print(myFruitList[0]) 
print(myFruitList[1]) 
print(myFruitList[2])

"""changing values in a list"""
myFruitList[2]="orange"
print(myFruitList)

"""E2-Defining a tuple"""
myFinalAnswerTuple=("apple", "banana","pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

"""Access Tuple"""
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

"""E3-Intro dict data type"""
myFavoriteFruitDictionary = {
    "Akua":"apple",
    "Saanvi":"banana",
    "Paulo":"pineapple"
}

print(" ")
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
print(" ")

"""Categorizing Values"""
"""Creating a mixed-type list"""
myMixedTypeList=[45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))