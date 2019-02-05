def simple_calc(a, b, opr):
        if opr == '+' or opr == 'add':
            return a + b
        elif opr == '-' or opr == 'sub':
            return a - b
        elif opr == '*' or opr == 'mul':
            return a * b
        elif opr == '/' or opr == 'div':
            return a / b
        else:
            print("Enter a correct operator")

x = simple_calc(7, 4, '-')
print(x)
