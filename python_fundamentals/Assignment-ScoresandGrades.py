from random import randint

def ScoresandGrades(arg):
    print "Scores and Grades"
    for i in range(0,arg):
        score = randint(60,100)
        if (score>= 60 and score <= 69):
            print "Score: "+ str(score) + " Your grade is D"
        elif (score>= 70 and score <= 79):
            print "Score: "+ str(score) + " Your grade is C"
        elif (score>= 80 and score <= 89):
            print "Score: "+ str(score) + " Your grade is B"
        elif (score>= 90 and score <= 100):
            print "Score: "+ str(score) + " Your grade is A"
        else:
            print "Incorrect input"

ScoresandGrades(10)
