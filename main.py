import math
print('we are calculating a circumference in centimetres')
# formula = 2πr
print("")
#numb1 = int(input('enter the first number: '))
number = int(input('enter the number: '))
unit = input('are you given a radius or diameter (r/d) ?: ')
measurement = input('what measurement are you given (cm, m, mm) ?: ')
if measurement == "mm":
    equation = number / 10
elif measurement == "m":
    equation = number * 10
elif measurement == "km":
    equation = number * 100
print("")
print('THE FORMULA IS: 2πr ')
print("")
if unit == "r":
    sum = 2 * math.pi * equation
    print(f'the circumference of a circle is {round(sum, 2)}cm')
elif unit == "d":
    sum = 2 * (number / 2) * math.pi 
    print(f'the circumference of a circle is {round(sum, 2)}cm')
else:
    print(f'{unit} is an invalid unit')
    

