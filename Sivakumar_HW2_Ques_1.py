
#Python Homework 2, Question 1
#Python Version 3.7.x
def calc_average(s1, s2, s3, s4, s5):
    
    average = (s1 + s2 + s3 + s4 + s5)/5

    return average

def determine_grade(score):

    if score>=90 and score<=100 :
        return 'A'
    elif score>=80 and score<=89:
        return 'B'
    elif score>=70 and score<=79:
        return 'C'
    elif score>=60 and score<=69:
        return 'D'
    elif score < 60:
        return 'F'
    else:
        return ' '

def main():

    s1 = float(input("Enter test score 1:"))
    s2 = float(input("Enter test score 2:"))
    s3 = float(input("Enter test score 3:"))
    s4 = float(input("Enter test score 4:"))
    s5 = float(input("Enter test score 5:"))

    print('Grade for Score 1:',determine_grade(s1))
    print('Grade for Score 2:',determine_grade(s2))
    print('Grade for Score 3:',determine_grade(s3))
    print('Grade for Score 4:',determine_grade(s4))
    print('Grade for Score 5:',determine_grade(s5))

    print('Average of all scores are ', calc_average(s1, s2, s3, s4, s5))




main()




