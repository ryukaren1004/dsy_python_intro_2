def computegrade(scoref):
    if scoref>1.0 or scoref<0:
        print('Bad Score')
    else:
        if scoref >= 0.9:
            grade = 'A'
        elif scoref >= 0.8:
            grade = 'B'
        elif scoref >= 0.7:
            grade = 'C'
        elif scoref >= 0.6:
            grade = 'D'
        else:
            grade == 'E'
    return grade;
try:
    score = input('Enter a score between 0.0 and 1.0: ')
    score = float(score)
    grade = none
    computegrade(scoref)
    print(ans)

except:
        print('Bad Score')
