#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to convert kilometers to miles?

# In[33]:


km = float(input("Enter kilometer"))

multiplier = 0.621371

print("%0.1f km is equal to %0.4f miles" %(km,km*multiplier))


# 2. Write a Python program to convert Celsius to Fahrenheit?

# In[37]:


celsius = float(input("Enter celsius number"))

fahrenheit = (celsius * 1.8) + 32

print("%0.2f celsius is equal to %0.4f fahrenheit" %(celsius,fahrenheit))


# 3. Write a Python program to display calendar?

# In[2]:


import calendar

year = int(input("Enter calendar year"))

month = int(input("Enter calendar month"))

if month >=1 and month <= 12 :
    print(calendar.month(year,month))
else :
    print("enter month is invalid")


# 4. Write a Python program to solve quadratic equation?

# In[14]:


import math

a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))

def quad_fn(a,b,c) :
    d = (b**2 - 4 * a * c)
    sq_r = math.sqrt(abs(b**2 - 4 * a * c))
    
    if d >= 0 :
        print(((- b + sq_r)/ 2 * a))
        print(((- b - sq_r)/ 2 * a))
    else :
        print ((- b/ 2*a), "+ i", (sq_r/ 2 * a))
        print ((- b/ 2*a), "- i", (sq_r/ 2 * a))
    


if a != 0 :
    quad_fn(a,b,c)
else :
    print("Value of a can not be zero")


# 5. Write a Python program to swap two variables without temp variable?

# In[49]:


a = int(input("Enter first number"))
b = int(input("Enter second number"))

a = a + b
b = a - b
a = a - b

print("first number after swap ", a)
print("Second number after swap", b)


# In[ ]:




