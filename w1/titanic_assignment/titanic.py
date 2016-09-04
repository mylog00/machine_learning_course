import pandas

# load data from csv
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
data = pandas.read_csv('titanic.csv', index_col='PassengerId')

# 1. Какое количество мужчин и женщин ехало на корабле?
# В качестве ответа приведите два числа через пробел.
male = 0
female = 0
for sex in data['Sex']:
    if sex == 'male':
        male += 1
    else:
        female += 1

print str(male) + ' ' + str(female)
