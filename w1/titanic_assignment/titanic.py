import pandas

# load data from csv
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
data = pandas.read_csv('titanic.csv', index_col='PassengerId')

passenger_number = len(data)

# 1. Какое количество мужчин и женщин ехало на корабле?
# В качестве ответа приведите два числа через пробел.
male = 0
female = 0
for sex in data['Sex']:
    if sex == 'male':
        male += 1
    else:
        female += 1
result = str(male) + ' ' + str(female)
# 577 314
print(result)

# 2.Какой части пассажиров удалось выжить? Посчитайте долю выживших пассажиров.
# Ответ приведите в процентах (число в интервале от 0 до 100,
# знак процента не нужен), округлив до двух знаков.
survive_counter = 0
for survived in data['Survived']:
    if survived:
        survive_counter += 1
result = (100 * survive_counter) / passenger_number
result = "{0:.2f}".format(result)
# 38.38
print(result)

# TODO
# 3.Какую долю пассажиры первого класса составляли среди всех пассажиров?
# Ответ приведите в процентах (число в интервале от 0 до
# 100, знак процента не нужен), округлив до двух знаков.

# 4. Какого возраста были пассажиры? Посчитайте среднее и медиану
# возраста пассажиров. Ответ приведите в процентах
# (число в интервале от 0 до 100, знак процента не нужен), округлив до двух
# знаков.

# 5. Коррелируют ли число братьев/сестер с числом родителей/детей?
# Посчитайте корреляцию Пирсона между признаками SibSp и Parch.

# 6. Какое самое популярное женское имя на корабле? Извлеките из
# полного имени пассажира (колонка Name) его личное имя (First Name).
# Это задание — типичный пример того, с чем сталкивается специалист
# по анализу данных. Данные очень разнородные и
# шумные, но из них требуется извлечь необходимую информацию.
# Попробуйте вручную разобрать несколько значений столбца Name
# и выработать правило для извлечения имен, а также разделения
# их на женские и мужские.
