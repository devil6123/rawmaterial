            # Calculator using python
# import math
# print("What kind of operation do you want to perform ")
# print("1:addition")
# print("2:multiplication")
# print("3:subtraction")
# print("4:division")
# print("5:square Root of any number")
# operation =int(input())
# if operation==1:
#     x=int(input("enter first value="))
#     y=int(input("enter second value="))
#     print(x+y)
# elif operation==2:
#     x=int(input("enter first value="))
#     y=int(input("enter second value="))
#     print(x*y)
# elif operation==3:
#     x=int(input("enter first value="))
#     y=int(input("enter second value="))
#     print(x-y)
# elif operation==4:
#     x=int(input("enter first value="))
#     y=int(input("enter second value="))
#     print(x/y)
# elif operation==5:
#     x=int(input("enter value="))
#     print(math.sqrt(x))
        
             # python functions
# def myfunction(fname,lname):
#     print(fname+" "+lname)
# myfunction("ali","raza")

# def addNum(a,b):
#     print(a+b)
# addNum(5,6)

# def tryRec(k):
#     if (k>0):
#         result=k + tryRec(k-1)
#         print(result)
#     else:
#         result=0
#     return result
# print("resursion")
# tryRec(7)

# lambda functons
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# import array as arr
# arr=[1,2,4,3,5,6,9,7]
# arr.sort()
# print(arr)

# reverse the order of an array
# arr.reverse()
# print(arr)
 
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# class Person:
#     def __init__(self,name,cast):
#         self.name=name
#         self.cast=cast
#     def data(self):
#         print(self.name,self.cast) 
# x=Person("ABC","XYZ")
# x.data()

# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }
				
# n = int(input())
# count  = 0
# while  n > 0:
#     n = n // 10
#     count = count + 1
# print(count)

# num = int(input("Enter the number"))

# digit = int(input("Enter a Digit"))

# count = 0

# n = num

# while n != 0:

#     rem = n % 10

#     if rem == digit:

#         count+=1

#     n = n // 10

# print("{} occured {} times in {}".format(digit,count,num))
# num=int(input("enter the number"))
# digit=int(input("enter the digit that you nwant to count"))
# count=0
# n=num
# while n>0:
#     rem=n%10 # 3
#     if rem==digit: # 3=3
#         count+=1
#     n=n//10
# print("{} occured {} times in {}".format(digit,count,num))

# num = int(input("enter a number"))
# n = num
# product = 1
# while n != 0:
#     rem = n % 10
#     product = product + rem
#     n = n // 10
# print(product)

# Python 3 program to
# compute sum of digits in
# number.

# Function to get sum of digits

# def getSum(n):
# 	sum = 0
# 	while (n != 0):
# 		sum = sum + int(n % 10)
# 		n = int(n/10)
# 	return sum

# # Driver code
# if __name__ == "__main__":
# 	n = 687

# 	# Function call
# 	print(getSum(n))

# n=int(input("enter the number"))
# sum=0
# while (n !=0):
# 	sum=sum+int(n%10)
# 	n=int(n/10)
# print(sum)

# num = int(input("enter a number"))
# n = num
# reverse = 0
# while n != 0:
#     rem = n % 10
#     reverse = reverse * 10 + rem
#     n = n // 10
# print("{} is reverse of {}".format(reverse, num))

#tuples
# names=("cli","ahmed")
# print(names)
# print(sorted(names))

# set

# set1={1,2,3,4,5,6,7}
# set2={3,5,6,7,8,4}
# intersect=set1 & set2
# print(intersect)
# union=set1 | set2
# print(union)
# set1={1,2,3,4,5,6,7}
# if 9 in set1:
#     print(True)

# functions in python
 
# def hello(name="hunny"): 
#it is a default arg if we do not pass the name at the time of function calling it will assign hunny to the name  
#     print("hello "+name)

# hello("babar")
# hello()

# def count():
#     count=0

#     def increament():
#         nonlocal count  
#         #The nonlocal keyword is used to work with variables inside nested functions, where the 
#         #variable should not belong to the inner function. Use the keyword nonlocal to declare that the variable is not local
#         count=count+1
#         print(count)
#     increament()

# count()


# items=[1,2,3,4,5]
# for item in enumerate(items):
#     print(item)


# items=[1,2,3,4,5,6]
# for item in items:
#     if item==4: # it will skip the numver 4 and cotinue iterating
#         continue
#     print(item) 



# class Activity:
#     def coding(self):
#         print("coding right now")

# class Person(Activity):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def data(self):
#         print("hello I am "+self.name+" my age is "+str(self.age))

# x=Person("babar",30)
# x.data()
# x.coding()   



# Accepting Arguments using command line
# import sys
# name=sys.argv[1]
# print("hello " + name)

# import sys 
# print(sys.argv)

# import argparse 
# parser=argparse.ArgumentParser(
#     description="this program------"
# )

# parser.add_argument('-c','--color',metavar='color', required=True,choices={'red','blue'
# },help='the color to search for')

# args=parser.parse_args()
# print(args.color)


           #  map,filter,reduc0
# numvbers=[2,3,4,5,6]
# def double(a):
#     return a*2
# result=map(double,numvbers)
# print(list(result))

# numvbers=[2,3,4,5,6]
# double=lambda a:a*2
# result=map(double,numvbers)
# print(list(result))

# numvbers=[2,3,4,5,6]
# result=map(lambda a:a*2,numvbers)
# print(list(result))


# number = [1,2,3,4,5,6]
# def isEven(n):
#    return n%2==0
# result=filter(isEven,number)
# print(list(result))

# number=[1,2,3,4,5,6]
# result=filter(lambda n:n%2==0,number)
# print (list(result))

      # Reduce
#The idea behind Python's reduce() is to 
#take an existing function, apply it cumulatively to all the items in an iterable,
#and generate a single final value
# from functools import reduce 
# expenses=[
#     ('dinner',300),
#     ('lunch',400)
# ]
# sum=reduce(lambda a,b:a[1]+b[1],expenses)
# print(sum)

# def factorial(n):
#     if n==1:return 1
#     return n*factorial(n-1)
# print(factorial(7))


# Armstromg number
# def power_1(A, B):  
        
#     if B == 0:  
#         return 1  
#     if B % 2 == 0:  
#         return power_1(A, B // 2) * power_1(A, B // 2)  
            
#     return A * power_1(A, B // 2) * power_1(A, B // 2)  
    
# # Function for calculating "order of the number"  
# def order_1(A):  
    
#     # Variable for storing the number  
#     N = 0  
#     while (A != 0):  
#         N = N + 1  
#         A = A // 10  
            
#     return N  
    
# # Function for checking if the given number is Armstrong number or not  
# def is_Armstrong(A):  
        
#     N = order_1(A)  
#     temp_1 = A  
#     sum_1 = 0  
        
#     while (temp_1 != 0):  
#         R_1 = temp_1 % 10  
#         sum_1 = sum_1 + power_1(R_1, N)  
#         temp_1 = temp_1 // 10  
    
#     # If the above condition is satisfied, it will return the result  
#     return (sum_1 == A)  
    
# # Driver code  
# A = int(input("Please enter the number to be checked: "))  
# print(is_Armstrong(A))  

        #decorators
# A decorator is a design pattern in Python that allows a user
# to add new functionality to an existing object without modifying its structure

# def logtime(func):
#     def wrapper():
#         print("before")
#         val=func()
#         print("after")
#         return val
#     return wrapper
# @logtime
# def hello():
#     print("hello")
# hello() 

# Annotations

# def increament(n:int)->int: # we are defining here that the function accept and return the value in in int
#     return n+1

#Exception handling
# try:
#     result=2/0
# except ZeroDivisionError:
#     print("can`t devide by Zero")
# finally:
#    result= 1

# print(result)


# class DogNotFoundexcecption(Exception):
#     print("inside")
#     pass
# try:
#     raise DogNotFoundexcecption()
# except DogNotFoundexcecption:
#     print("Dog Not found")

# f = open("New Text Document.txt", "w")
# f.write("Now the file has more content!")
# # print(f.read())
# f.close()

# f = open("New Text Document.txt", "r")
# print(f.read())
# f = open("myfile.txt", "x")
# f = open("myfile.txt", "w")
# f.write("Now the file has more content!")
# print(f.read())

# import camelcase

# c = camelcase.CamelCase()

# txt = "hello world"
# # print(c.txt)
# print(c.hump(txt))

# list compressions
# numbers=[1,2,3,4,5,6]
# numbers_power_2=[n**2 for n in numbers]
# print(numbers_power_2)

# # polymouphism
# class Dog:
#     def eat(self):
#         print("eating dog found")
# class Cat:
#     def eat(self):
#         print("eating cat found")

# animal1=Dog()
# animal2=Cat()

# animal1.eat()
# animal2.eat()

# dept={"HR":["ali","abrar","ahmed"],"finance":["adnan","kami","umar"]}
# dept["accounts"]=["saad","kashan"]
# print(dept.get("accounts"))