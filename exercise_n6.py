
def compute_total_average(eng, mat):
    res = mat+eng

    return res

english = input("Enter English score: ")
english = int(english)


math = input("Enter Math score: ")
math = int(math)

total = compute_total_average(english, math)
average = compute_total_average(english, math)/2

print('total =',total)
print('average =',average)
