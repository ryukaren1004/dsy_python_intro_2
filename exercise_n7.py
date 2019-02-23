
def computegrade(scoref):
    sc = scoref
    if sc>1.0 or sc<0:
        grade = 'Bad Score'
    else:
        if sc >= 0.9:
            grade = 'A'
        elif sc >= 0.8:
            grade = 'B'
        elif sc >= 0.7:
            grade = 'C'
        elif sc >= 0.6:
            grade = 'D'
        else:
            grade == 'E'
    return grade;
try:
    score = input('Enter a score between 0.0 and 1.0: ')
    score = float(score)
    ans = computegrade(score)
    print(ans)

except:
    print('Bad Score')
