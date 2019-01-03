# Python Assignment


## Part 0: Fork and clone the repo

You should make your own copy of the repository so that you can edit it and at the end submit a pull request.

1. Create a fork of this repo by clicking on the **Fork** link in the upper right.
2. Checkout your personal copy of the repo: `git clone https://github.com/<username>/python-intro1`

### How to submit?
1. `git add filename` (or `git add .`) for all the files you want to add.
2. `git commit -m "Message describing what you did"`
3. `git push origin master`
4. Now if you go to your personal copy on github, your changes should be there: `https://github.com/<username>/python-intro1`
5. From there, click on **Pull Requests** and then **New pull request**.

Ideally, you should regularly run steps 1-3. This will save your work as you go. And if you ever goof things up, you will have all the history, you can revert any file to how it was at any previous commit!

## Exercise 
1. Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.
Using atom text editor, open ./src/assignment_2.1.py and write your program.
<br>Compare your output with 'Desired Output'

    Desired Output: 
            <b>Pay: 96.25</b>
                 
2.1. Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
Using atom text editor, open ./src/assignment_2.2.1.py and write your program.
<br>Compare your output with 'Desired Output'

    Desired Output: 
            <b>Pay: 498.75</b>

2.2 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
'>= 0.9 A
'>= 0.8 B
'>= 0.7 C
'>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.            

Using atom text editor, open ./src/assignment_2.2.2.py and write your program.
<br>Compare your output with 'Desired Output'

    Desired Output: 
            <b>B</b>


And then submit it as above submit guide. 

