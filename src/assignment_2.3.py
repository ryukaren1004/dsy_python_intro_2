

def compute_total_average(eng, mat, stat):
    if stat == 'total':
        res = eng + math
    elif stat == 'average':
        res = (eng+math)/2
    else:
        res = None

    return res

english = input("Enter English score: ")
english = int(english)

# Write your code here
math = input("Enter Math score: ")
math = int(math)

total = compute_total_average(english, math, 'total')
average = compute_total_average(english, math, 'average')

print('total =',total)
print('average =',average)
