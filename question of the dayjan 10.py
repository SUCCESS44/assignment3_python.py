#1.write a python function to find the max of 3 numbers.
from os import lseek


n1=int(input ("Enter first number:"))
4
n2=int(input("Enter second number:"))
12
n3=int(input("Enter third number:"))
8
def f():
    if(n1>=n2) and (n1>=n3):
      l=n1
    elif(n2>=n1) and (n2>=n3):
      l=n2
    else:
      l=n3
    print("Largest number among the three is",l)
f()
#2. Write a python function to sum all the numbers in a list.
def sum(num):
    sum = 0
    for i in num:
     sum+= i
    return sum
list = [1,2,3,4]
print(sum((list)))
#3. Write a python function to multiply all numbers in a list
list1 = [3,2,4]
def multiplylist(mylist):
    result = 1
    for x in mylist:
        result = result * X
    return result
print(multiplylist)(list1)        
#4. Write a python function to reverse a given string.
s = "mylaptopisgood"
def reverse(s):
    str = ""
    for i in s:
     str = i + str
    return str
print("The original string is:", end="")
print(s)
print(reverse(s))
#5. Write a python function that takes a string and displays the number of upper case letters and the number of lower case letters.
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
     if c.isupper():
      d["UPPER_CASE"]+=1
     elif c.islower():
       d["LOWER_CASE"]+=1
     else: 
      pass
    print("The original string : ", s)
    print("No of Upper case characters : ", d["UPPER_CASE"])
    print("No of Lower case charaters : ", d["LOWER_CASE"])
string_test("Okere is Good Always")
#Question of the day Jan 11
#Create a function func() which takes a variable number of arguments and prints out those variables.
#So for example if func(23, 25, 25)
#it should print 23, 25, and 25,
#if func(20, 21)
#it should print 20, 21
numbers = (23,25,25)
def vaiables_numbers():
    print(numbers)
 #Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction.
#Also, it must return both addition and subtraction in a single return call.
def func(num1, num2): 
     sum_ = num1+num2
     sub_ = num1-num2
     return sum_, sub_
func(22,10)
#Write a program to create a function show_employee() using the following conditions.
#It should accept the employee’s name and salary and display both.
#If the salary is missing in the function call then assign default value 9000 to salary
def fargate(employee, salary = 9000):
    print('employee: ', employee)
    print('salary: ', salary)
fargate('okere', 6000)
