<b>Exercise 1: Run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get.</b>

The random function is only one of many functions that handle random numbers. The function randint takes the parameters low and high, and returns an integer between low and high (including both).

    >>> import random
    >>> random.randint(5, 10)
    >>> random.randint(5, 10)
    >>> random.randint(5, 10)
    To choose an element from a sequence at random, you can use choice:

<b>Exercise 2: Move the last line of below program to the top, so the function call appears before the definitions. Run the program and see what error message you get.</b>

    >>> repeat_name_printing('Alex', 'Seong')
    
    >>> def print_my_name(fname, lname=''):
    ...     print("My name is ", fname)
    ...     print("My full name is ", fname, lname)

    >>> def repeat_name_printing(fname, lname=''):
    ...    print_my_name(fname, lname)
    ...    print_my_name(fname, lname)


<b>Exercise 3: Move the function call back to the bottom and move the definition of print_my_name after the definition of repeat_name_printing. What happens when you run this program?   
    
    >>> def repeat_name_printing(fname, lname=''):
    ...    print_my_name(fname, lname)
    ...    print_my_name(fname, lname)

    >>> def print_my_name(fname, lname=''):
    ...     print("My name is ", fname)
    ...     print("My full name is ", fname, lname)

    >>> repeat_name_printing('Alex', 'Seong')



<b>Exercise 2: Rewrite your weighted average computation program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:</b>

    Enter English Score: 95
    Enter Math Score: Eighty-Five
    Error, please enter numeric input
    Enter English Score: Ninety
    Error, please enter numeric input

<b>Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:</b>

     Score   Grade
    >= 0.9     A
    >= 0.8     B
    >= 0.7     C
    >= 0.6     D
     < 0.6     F
    Enter score: 0.95
    A
    Enter score: perfect
    Bad score
    Enter score: 10.0
    Bad score
    Enter score: 0.75
    C
    Enter score: 0.5
    F
Run the program repeatedly as shown above to test the various different values for input.