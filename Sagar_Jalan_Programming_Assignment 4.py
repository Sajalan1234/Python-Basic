#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Write a Python Program to Find the Factorial of a Number');get_ipython().run_line_magic('pinfo', 'Number')
get_ipython().set_next_input('2. Write a Python Program to Display the multiplication Table');get_ipython().run_line_magic('pinfo', 'Table')
get_ipython().set_next_input('3. Write a Python Program to Print the Fibonacci sequence');get_ipython().run_line_magic('pinfo', 'sequence')
get_ipython().set_next_input('4. Write a Python Program to Check Armstrong Number');get_ipython().run_line_magic('pinfo', 'Number')
get_ipython().set_next_input('5. Write a Python Program to Find Armstrong Number in an Interval');get_ipython().run_line_magic('pinfo', 'Interval')
get_ipython().set_next_input('6. Write a Python Program to Find the Sum of Natural Numbers');get_ipython().run_line_magic('pinfo', 'Numbers')


# 1. Write a Python Program to Find the Factorial of a Number?

# In[9]:


num = int(input("Enter a number"))

mul = 1
for i in range(1,num+1) :
    mul = mul * i

print("Factorial of number %s is %s" %(num,mul))


# 2. Write a Python Program to Display the multiplication Table?

# In[11]:


num = int(input("Enter a number"))

mul = 1
for i in range(1,11) :
    print(num, "*" ,i, "=", num*i )


# 3. Write a Python Program to Print the Fibonacci sequence?

# In[20]:


num = int(input("Enter size of the series "))

a = 0
b = 1
                        
for i in range(num) :
    print(a , end =" " )
    a, b = b , a + b


# 4. Write a Python Program to Check Armstrong Number?

# In[32]:


num = int(input("Enter the number "))
length = len(str(num))
sum = 0
temp = num

while num > 0 :
    n = num % 10
    sum = sum + n**length
    num = int(num/10)

if sum == temp :
    print("Armstrong number")
else :
    print("Not Armstrong number")


# 5. Write a Python Program to Find Armstrong Number in an Interval?

# In[31]:


l1 = int(input("Enter the starting point of interval "))
l2 = int(input("Enter the ending point of interval "))
def arms(num) :
    length = len(str(num))
    sum = 0
    temp = num

    while num > 0 :
        n = num % 10
        sum = sum + n**length
        num = int(num/10)
    
    if sum == temp :
        return True
    else :
        return False
    
for i in range(l1,l2+1) :
    if arms(i) :
        print(i, end = " ")
        
    
        


# 6. Write a Python Program to Find the Sum of Natural Numbers?

# In[34]:


num = int(input("Enter the number "))

sum = 0
for i in range(1,num+1) :
    sum = sum + i

print(sum)


# In[ ]:




