#!/usr/bin/env python
# coding: utf-8
1. What exactly is []?

[] is called index bracktet or sqare bracket, It has many used in python, It is used to design a list and its allowing to declare a list and content of list. It is also used to express an expression, it is also used to extract data from list,tuples,string and dictionary with the help of index(address).It can be also called empty list value.2. In a list of values stored in a variable called spam, how would you assign the value "hello" as the
third value? (Assume [2, 4, 6, 8, 10] are in spam.)

With the help of insert() fn which is in-build fn of list object, we can inster any value at any position inside a list.
insert fn takes two arguments one is position and the 2nd one is Value.

spam = [2,4,6,8,10]
spam.insert(2,"hello")
# Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.

# In[5]:


spam  = ['a', 'b', 'c', 'd'] 

3. What is the value of spam[int(int('3' * 2) / 11)]?

  spam[int(int('3' * 2) / 11)]
#spam[int(int('33') / 11)]
#spam[int(33 / 11)]
#spam[3] == output will be "d"4. What is the value of spam[-1]?

Value of spam[-1] = 'd'5. What is the value of spam[:2]?

value of spam[:2] = ['a', 'b']
# Let's pretend bacon has the list [3.14," cat", 11,' cat', True] for the next three questions.

# In[20]:


bacon = [3.14,'cat', 11,'cat',True] 

6. What is the value of bacon.index('cat')?

# index function is a in-build fn of list which gives the position of first occurence of given value inside the list.
bacon.index('cat') = 17. How does bacon.append(99) change the look of the list value in bacon?

append() fn is a inbuilt fn of list object which add the given value inside the lis at the last index or position of the list.

bacon.append(99) = result = 99 will add at the last index of bacon list like [3.14,'cat', 11,'cat',True, 99]8. How does bacon.remove('cat') change the look of the list in bacon?

remove() fn is a in-built fn of list object which will remove the first occurence of the given value from the list.

bacon.remove('cat') = result = 'cat' at index 1 will remove from bacon list like [3.14, 11,'cat',True]
# In[ ]:


get_ipython().set_next_input('9. What are the list concatenation and list replication operators');get_ipython().run_line_magic('pinfo', 'operators')

To join two or more list(or list concatenation), we can use the + operator. + list concatenation operator
To multiply the list a given number of times(or replication), we can use the * operator. * list replication operator

10. What is difference between the list methods append() and insert()?

append() fn is a inbuilt fn of list object which add the given value inside the list at the last index or position of the list.
It takes only one argument. syntax - list_name.append(value).
with the help of append operation we can only add data to list at last position.

insert() fn is in-build fn of list object, we can inster any value at any position inside a list. insert fn takes two 
arguments one is position and the 2nd one is Value. syntax -  list_name.insert(position,value)
with the help of insert operation we can add data to list at any position.11. What are the two methods for removing items from a list?

pop() - fn is in-build fn of list object which remove the value from the given position inside the list.and if we didn't give
the position then it will remove the value from the last position.
It may or may not takes one argument. syntax - list_name.pop(position).

remove() fn is a inbuilt fn of list object which remove the given value from the list. It takes only one argument. 
syntax - list_name.remove(value).12. Describe how list values and string values are identical.

list and string are two different thing but is some part they are identical:-
    1. we can get length of both list and string with the help of len() fn,
    2. list and sring both have indexes and starting at 0,
    3. both will follow same concatenation and replication process, means both will do with concatenation and replication with
        same datatype value,
    4. In both we can perform slicing operation13. What's the difference between tuples and lists?

List are mutable or we can say changeble means value can be add or remove from the list 
                                but
Tuples are immutable or we can say unchangeble means once we create a tuples value cann't be add or remove from the tuples.

List are represent using square bracketl[] whereas tuples are represent  using parenthesis t()14. How do you type a tuple value that only contains the integer 42?

To create a tuple which contain only one value, we need to add a comma after the value othjerwise compiler will take it as a
integer value
t = (42,)15. How do you get a list value's tuple form? How do you get a tuple value's list form?

To get a list valve from the tuple, we need to call a list() fn and pass the tuple as an an argument to that list fn or 
we can say we need to do type casting of that tuples to the list --> l = list(tuple_name)

To get a tuple valve from the list, we need to call a tuple() fn and pass the list as an an argument to that tuple fn or 
we can say we need to do type casting of that list to the tuple --> t = tuple(list_name)16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?

Generally they contain reference to list values.17. How do you distinguish between copy.copy() and copy.deepcopy()?

In deep copy(copy.deepcopy()) any changes made to the copy of an object do not reflect to the original object.

In shallow copy(copy.copy()), a reference of an object is created. means any changes made to the referenced object will 
also reflect to the original object.