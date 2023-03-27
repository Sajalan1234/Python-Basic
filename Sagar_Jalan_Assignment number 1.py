#!/usr/bin/env python
# coding: utf-8

# # Assignment # 1
1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.

*           --> Expression(because its a mathmatical operator)
'hello'     --> Value(string datatype value)
-87.8       --> Value(float datatype value)
-           --> Expression(because its a mathmatical operator)
/           --> Expression(because its a mathmatical operator)
+           --> Expression(because its a mathmatical operator)
6           --> Value(Integer datatype value)2. What is the difference between string and variable?

String is a text which is written within the single quotes('') or double quotes(" ").If we write any thing within a quotes its
treated as string. It can alpha value,numerical value,alpha numerical value or any special characters.
E.g -- "Sagar", "123", "sag123", "@", " " etc 

Whereas, A variable is a name which we assign to any type of data or we can say variable is a place where we store a different type of data to it. Variable will also allocate memory depends on which type of data we are storing in given variable.
variable name will start with either alphan or underscore only.
sring, integer, decimal, Boolean these are some example of data which we can assign to  variable.
E.g -- name = "sagar"  , Age = 25 , salary = 3.5, temp = True3. Describe three different data types.

Numerical datatype - It is used to hold numerical value like int(hold =ve or -ve namtural number, float(hold integer value) & 
                     complex(hold the complex number). 
                                                                 
Sequence datatype -  It store collections of similar or different types.It store data with its index value form Like list, tuple
                                                                 
Boolean datatype -   It store only two build-in values True & False. True is represent truth or 1 and False represent fail or                        0.
                     4. What is an expression made up of? What do all expressions do?

Expression is made up of different combination of operator & operands(can be string,list integer function object etc).
Expression is used to find some required value.
Ex - x = x + 105. This assignment statements, like spam = 10. What is the difference between an expression and a statement?

In python statement is a line of code which execute a line of instruction or we can say it tells the computer to perform a task.

Expression is a combinations of operators & operands. if we assign a result of an expression to a varible, then that line of code can be a statements, means all expression can become a stament but all statement cann't be a expression.

In the above example spam = 10 --> we tells the computer to assign 10 to a varible, its a staement not an expression. 6. After running the following code, what does the variable bacon contain?

bacon = 22 # with the help of this statment bacon(name of a variable) will assign a value 22. bacon has int datatype
bacon + 1  # with the help of this statment 22 is added with 1 and result output will be give as 23

But still value of bacon is 22 because we are not assigning the above result to bacon7. What should the values of the following two terms be?

'spam' + 'spamspam' # The plus operator is act as a concatenation for given two string.
                    # value = 'spamspamspam'

'spam' * 3          #   The * operator is act as a multiplies between string and number.And string will become three times.
                    # value = 'spamspamspam'8. Why is eggs a valid variable name while 100 is invalid?

According to nomenclature given for variable by Python's creater is variable name will either start with alphabet or 
underscore(_) only. So, eggs a valid variable name while 100 is invalid9. What three functions can be used to get the integer, floating-point number, or string
version of a value?

int(), float(), str() - these are the three functions used to to get the integer, floating-point number, or string
version of a value.10. Why does this expression cause an error? How can you fix it?
'I have eaten' + 99 + 'burritos.' # in this expression we are trying to perform concatenation operation between the strings 
                                    and numerical value but we can perform concatenation between the same datatype valiable.
                                    thats why it gives us error.

To fix this error we need to to do type casting with the numerical value and convert it into string.
'I have eaten' + str(99) + 'burritos.' 