#!/usr/bin/env python
# coding: utf-8

# In[ ]:




1.What are the two values of the Boolean data type? How do you write them?
Two values of boolean data type are True and False, True value is similar to 1 and False value is similar to 0.

a = True
b = False2. What are the three different types of Boolean operators?

and - Return true only if its both side values is true

or  - Return true if any of its the both side value is true\

not - its reverse the value means if result is true then after using it result will be false and vice-versa3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).

and >   _  and  _    =  Result
      True  |  True  -   True
      True  |  False -   False
      False |  True  -   False
     False  |  False -   False
        
or >   _    or _     =  Result
      True  |  True  -   True
      True  |  False -   True
      False |  True  -   True
     False  |  False -   False
        
not >   not(True)    -   False
        not(False)   -   True4. What are the values of the following expressions?
(5 > 4) and (3 == 5)                  = (5 > 4)- true, (3 == 5)- false So, True and False = False(ans)
not (5 > 4)                           = not(True) = False(ans)
(5 > 4) or (3 == 5)                   = True or False = True(ans)
not ((5 > 4) or (3 == 5))             = not(True or False) - not(True) = False(ans)
(True and True) and (True == False)   = True and False = False(ans)
(not False) or (not True)             =True or False = True(ans)5. What are the six comparison operators?

 ==       Equal to
 !=       Not equl to
 <        Less than
 <=       Less than or equal to
 >        Greater than
 >=       Greater than or equal to6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.

Syntax of equal to operator   : ==  -> it will check whether the right side value and the left side value is same or not.
                                       Its generally used for condition operator and its output is either "True" or "False"
        
Syntax of assignment operator : =   -> it will assign the right side operand to the left side variable or operand.
                                       Its generally used to save a value to another value
        
Example :-   spam = 0          # 0 is assign to a variable spam
             if spam == 0 :    # its checking either spam value is zero or not
                spam = 1       # 1 is assign to a variable spam7. Identify the three blocks in this code:
spam = 0
if spam == 10:      # Block 1
    print("eggs")
if spam > 5:        # Block 2
    print("bacon")
else:               # Block 3
    print("ham")
    print("spam")
    print("spam")
# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
# Greetings! if anything else is stored in spam.

# In[ ]:


spam = int(input("enter number"))
if spam == 1:     
    print("Hello")
elif spam ==2 :       
    print("Howdy")
else:               
    print("Greeting!")

9.If your programme is stuck in an endless loop, what keys you’ll press?

To stop infinite loop we need to press "ctrl + c" to stop the infinite loop or need to restart por interrupt the kernel.10. How can you tell the difference between break and continue?

Let us understand it with the help of for loop example :-
    for i in range(4) :
        if i == 2 :
            break
        print(i, end = (" "))     # output - 0, 1

If we execute the above code then once value of i equal to 2 its satisfy the if condition and break statememnt will execute
and we completely come out from the for loop.Means once the break statement will execute it will stop the next whole iteration 
and the cursor will come out from the inner loop or inner loop will stop execution.

    for i in range(4) :
        if i == 2 :
            continue
        print(i, end = (" "))    # output - 0, 1, 3
        
If we execute the above code then once value of i equal to 2 its satisfy the if condition and continue statememnt will execute
and it will move the cursor to again for loop.Means once the continue statement will execute it will stop the current iteration
(next statment will not execute)and the cursor will pointing the loop.11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

There is no differences between the above given three range function. In all above three index will start from zero(0) and 
move in forward or positive direction with step of one till the last position or index 9th, here in function last index is 
given as 10 but its exluded.
# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
# program that prints the numbers 1 to 10 using a while loop.

# In[11]:


# using for loop
for i in range(1,11) :
    print(i, end = (" "))


# In[13]:


# using while loop
i = 1
while i < 11 :
    print(i, end = (" "))
    i = i + 1


# In[20]:


for i in range(4) :
       if i == 2 :
           continue
       print(i, end = (" "))

13. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?

spam.bacon()