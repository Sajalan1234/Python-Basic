#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to print "Hello Python"?

# In[2]:


def dis_hello() :
    print("Hello Python")
    
dis_hello()


# 2. Write a Python program to do arithmetical operations addition and division.?

# In[3]:


a = int(input("Enter first number"))
b = int(input("Enter second number"))

def sum(a,b) :
    return a+b

def div(a,b) :
    try :
        return a/b
    except Exception as e :
        return(e)

print(sum(a,b))
print(div(a,b))


# 3. Write a Python program to find the area of a triangle?

# In[4]:


b = int(input("Enter base"))
h = int(input("Enter height"))

def area(b,h) :
    return (b*h)/2

print(area(b,h))


# 4. Write a Python program to swap two variables?

# In[6]:


a = int(input("Enter first number"))
b = int(input("Enter second number"))

temp = a
a = b
b = temp

print("first number after swap ", a)
print("Second number after swap", b)


# 5. Write a Python program to generate a random number?

# In[14]:


import random
print(random.random())
print(random.randrange(1,100))

