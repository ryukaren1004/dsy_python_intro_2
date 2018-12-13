import sys, string

### Fill in each function below.

### Run "python -m doctest 3_fizzbuzz.py" at the command line to test your work.

def fizzbuzz(num, fizz=3, buzz=5):
    '''
    INPUT: int, int, int
    OUTPUT: string

    Return "Fizz" if num is divisible by fizz,
           "Buzz" if num is divisible by buzz,
           "FizzBuzz" if num is dibisible by both fizz and buzz, and
           "" otherwise

    Example:
    >>> fizzbuzz(15, 3, 5)
    'FizzBuzz'
    >>> fizzbuzz(10, 3, 5)
    'Buzz'
    >>> fizzbuzz(40, 20, 33)
    'Fizz'
    >>> fizzbuzz(15, 7, 13)
    '''

    if num % fizz == 0 and num % buzz == 0:
        return "FizzBuzz"
    elif num % fizz == 0:
        return "Fizz"
    elif num % buzz == 0:
        return "Buzz"
    else:
        return ""

if __name__ == '__main__':
#    if len(sys.argv) >= 2 and isnumeric(sys.argv[1]):
    if len(sys.argv) >= 2 and unicode(sys.argv[1], "utf=8").isnumeric():
#        print fizzbuzz(int(sys.argv[1]), 3, 5)
        print fizzbuzz(int(sys.argv[1]))
