import math as m

"""CONSTRUIR UM PROJETO QUE UNA TODOS OS EXERCICIOS DO PYTHON BRASIL EM UM SÓ CANTO"""

"""EX 01"""
def hello_world(language):
    if language == 1:
        return print("olá mundo!".capitalize())
    elif language == 2:
        return print("hallo welt!".capitalize())
    elif language == 3:
        return print("hola mundo!".capitalize())
    elif language == 4:
        return print("salut tout le monde!".capitalize())
    elif language == 5:
        return print("merhaba dunya!".capitalize())
    else:
        return print("hello world!".capitalize())

"""EX 02"""
def number_is(number):
    return print("The number reported was {}.".format(number))

"""EX 03"""
def sum_numbers(number_one, number_two):
    return number_one+number_two

"""EX 04"""
def grades_average(grades_quantity):
    grades = []
    for i in range(grades_quantity):
        grades += [float(input("Grade number {:.2f}: ".format((i+1))))]
    average = sum(grades)/grades_quantity
    return average


"""EX 05"""
def m_to_cm(meters):
    centimeters = 100*meters
    return centimeters


"""EX 06"""
def circle_area(radius):
    area = 2 * m.pi * pow(radius,2)
    return area


"""EX 07"""
def square_area(side1, side2):
    area = side1 * side2
    return area

def double_area(area):
    return area*2

"""EX 08"""

def gross_salary():
    earn_per_hr = float(input("How much you earn per hour? "))
    hours_worked = int(input("The number of hours worked in the month: "))
    gross = earn_per_hr * hours_worked
    return gross

"""EX 09"""

def fahr_to_celsius():
    fahrenheit = float(input("How many degrees fahrenheit do you want to convert? "))
    celsius = 5 * ((fahrenheit-32)/9)
    return celsius

"""EX 10"""

def celsius_to_fahr():
    celsius = float(input("How many degrees celsius do you want to convert? "))
    fahrenheit = (9*celsius)/5 + 32
    return fahrenheit

"""EX 11"""

def calculate_and_show():

    txt1 = "Integer: "
    txt2 = "Real Number: "
    integer_one, integer_two, real_number = int(input(txt1)), int(input(txt1)), float(input(txt2))

    a = (integer_one*2) * (integer_two/2)
    b = (integer_one*3) + real_number
    c = pow(real_number,3)

    print("The product double the first number with half of the second number is: {:.1f}".format(a))
    print("The sum of three times the first number with the third number is: {}".format(b))
    print("The third number raised to the cube is: {:.3f}".format(c))

"""EX 12"""
def perfect_weight_men():
    height = float(input("What is your height? "))
    good_weight = (72.7*height) - 58
    return good_weight

"""EX 13"""
def perfect_weight_women():
    height = float(input("What is your height? "))
    good_weight = (62.1*height) - 44.7
    return good_weight

def perfect_weight():
    sex = int(input("What sex? [1] XY or [2] XX: "))
    if sex == 1:
        return perfect_weight_men()
    elif sex == 2:
        return perfect_weight_women()
    else:
        return None 

"""EX 14"""
#é solicitado as variaveis em lingua portuguesa no exercicio
def papo_de_pescador():

    peso= float(input("Fish Weight: "))
    excesso = peso - 50
    multa = 4*excesso
    return multa  

"""EX 15"""
def liquid_salary():

    gross = gross_salary()
    income_tax = gross*0.11
    social_security = gross*0.08
    labor_union = gross*0.05
    liquid = gross - income_tax - social_security - labor_union
    
    txt = """+ Gross Salary: $ {:.2f}
- Income Tax: $ {:.2f}
- Social_security: $ {:.2f}
- Labor Union: $ {:.2f}
= Liquid Salary: $ {:.2f}"""
    
    print(txt.format(gross,income_tax,social_security,labor_union,liquid))   

"""EX 16"""
def paint_store_01():

    size_m2 = float(input())
    liters = size_m2/3

    if liters%18 != 0:
        liters += 1
    cans = int(liters / 18)
    total_prize = float(cans*80)

    return print("""{} cans have to be bought for {} m2 of coverage
    You have to pay ${}:.2f """.format(cans,size_m2,coverage))

"""EX 17"""
def total_gallons(t):
    area = float(input())
    liters = area / 6

    if t == True:
        if liters%18 != 0:
            liters += 1
            gallons = liters/18
    elif t == False:
        if liters%3.6 != 0:
            liters+=1
            gallons = liters/3.6
    else:
        gallons = -1

    return gallons

def situation_01(gallons):
    total_prize = float(gallons * 80)
    return total_prize

def situation_02(gallons):
    total_prize = float(gallons*25)
    return total_prize

def situation_03():
    return

"""EX 18"""
def download_time():
    download_size = float(intput("Size (MB) = "))
    Mbps = float(input("Mbps = "))

    MBs = Mbps * 0.125
    time = download_size / MBs

    return time