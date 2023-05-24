# a =2
# b=1
# if a < b:
#     print("b is greater than a")
# else:
#         print("a is greater than b")
    
    #Get the characters from position 2 to position 5 (not included):
# 
# b="hello wotrld"
# print(b[2:5]) 
# 
#Get the characters from the start to position  (not included):
# b="hello world"
# print(b[:6])
#Get the characters from position 2, and all the way to the end:
#b="hello world"
#print(b[2:])
#The strip() method removes any whitespace from the beginning or the end
# a = " Hello, World! "
# print(a.strip())
# The replace() method replaces a string with another string
# a= "babar Memon"
# print(a.replace("babar Memon","Babar Ali Memon"))
# txt="Hello babar how are you"
# print(txt)
# print(txt.replace("how","who"))
# a="babar"
# b="Memon"
# print(a+" "+b)

# Use the format() method to insert numbers into strings
# age=22
# tx="hello mt name is ahmed and i am {}"
# print(tx.format(age))

              # Lists are used to store multiple items in a single variable.
# fruits=["Apple","banana","kiwi"]
# print(fruits)
# Since lists are indexed, lists can have items with the same value
# fuirts=["apple","banana","kiwi","apple"]
# print(fuirts)
# A list can contain different data types
# data=["ali",22,False]
# print(data)
# You can specify a range of indexes by specifying where to start and where to end the range
# fuirts=["apple","banana","kiwi","apple"]
# print(fuirts[1:3]) # form a to b excluding b
# To determine if a specified item is present in a list use the in keyword
# fruits=["apple","banana","kiwi","apple"]
# if "appl" in fruits :
#     print("yes there is an apple present in the iist")
# else:
#     print("there is not any apple in the list")
# Using the append() method to append an item it ad the element at the end of an list
# fruits=["apple","banana"]
# fruits.append("orange")
# print(fruits)
# cars=["mehran","civic","cultus"]
# i=0
# while i<len(cars):
#     print(cars[i])
#     i=i+1
#print table
# x=0
# y=3
# while x <11:
#     print(x*y)
#     x=x+1
# Even and odd numbers
# x="pynative"
# i=0
# while i< len(x):
#    print(x[i])
#    i=i+2

# numbers_x = [10, 20, 30, 40, 10]
# size =len(numbers_x)
# if numbers_x[0]==numbers_x[size-1]:
#         print("numbers are same")
 

# numbers= [10, 20, 33, 46, 55]
# i=0
# while i < len(numbers):
#     if numbers[i]%5==0:
#         print(numbers[i])
#     i=i+1   
# str_x = "Emma is good developer. Emma is a writer"
# print(str_x.count("Emma")) 

# for i in range(10,0):
#     for j in range(i-1,0):
#            print("* ", end="")    
#     print()

# import array as arr 
# arr=["ahmed","abc","xyz"]
# print(arr.remove("babar"))

# origList=[12, 35, 9, 56, 24]
# temp=origList[0]
# x=len(origList)-1
# origList[0]=origList[x]
# origList[x]=temp
# print(origList)

# origList=[12, 35, 9, 56, 24]
# origList[0],origList[-1] = origList[-1],origList[0]
# print(origList)

# list = [1, 2, 5, 3, 4]
# a, *b, c = list
# print(a)
# print(b)
# print(c)

# import calc
# a=calc.person1["age"]
# print(a)

