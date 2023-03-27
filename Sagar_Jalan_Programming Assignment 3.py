#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[15]:


num = int(input("Enter a number"))

if num > 0 :
    print("positive number")
elif num == 0:
    print("Zero number")
else :
    print("negative number")


# 2. Write a Python Program to Check if a Number is Odd or Even?

# In[16]:


num = int(input("Enter a number"))

if num%2 == 0 :
    print("Even number")
else :
    print("Odd number")


# 3. Write a Python Program to Check Leap Year?

# In[72]:


year = int(input("Enter calendar year"))

if year % 100 == 0 and year % 400 == 0 :
    print("leap year")
elif year % 100 != 0 and year % 4 == 0 :
    print("leap year")
else :
    print("not leap year")


# 4. Write a Python Program to Check Prime Number?

# In[62]:


num = int(input("Enter a number"))

flag = 0

for i in range(2,num) :
    if num % i == 0  :
        flag = 1

if flag == 0 or num ==2 :
    print("prime number")
    
if flag == 1 :
    print("Not prime number")


# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[69]:



def prime(i) :
    flag = 0

    for j in range(2,i) :
        if i % j == 0  :
            flag = 1

    if flag == 0 or i ==2 :
        return True

    if flag == 1 :
        return False
    
for i in range(1,10001) :
    if prime(i) :
        print(i, end = " ")

