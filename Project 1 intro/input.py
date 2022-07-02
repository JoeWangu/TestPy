import math

def intro_py():
    course = "python for beginners"
    print(course.upper())
    print(course.find("b"))
    print("python" in course)
    full_name="John Smith"
    age=20
    is_new=True
    print(full_name[1:-1])
    print(len(full_name))


def input_py():
    name = input("What is your name? ")
    color = input("What is your favourite color ")
    print(name+" likes "+color)

    birth_year = input("Birth year: ")
    print(type(birth_year))
    age = 2021 - int(birth_year)
    print(age)

    weight_lbs = input("What is your weight (lbs): ")
    weight_kgs = int(weight_lbs) * 0.45
    print(weight_kgs)


def py_math_functions():
    x = 10 + 3 * 2 ** 2
    print(x)

    x=5.8
    print(round(x))

    x= -2.9
    print(abs(x))

    x = 5
    print(math.sin(x))


def if_operations():
    is_hot = True
    is_cold = False
    if is_hot:
        print("it's a hot day")
        print("drink plenty of water")
    elif is_cold :
        print("it's a cold day")
        print("wear warm clothes")
    else:
        print("it's a lovely day")
    print("enjoy your day")

    price = 1000000
    has_good_credit = True
    if has_good_credit :
       down_payment = 0.1 * price
    else :
        down_payment = 0.2 * price
    print(f"down payment: ${down_payment}")

    name = input("write your name ")
    if len(name) < 3:
        print("name must be at least 3 characters long")
    elif len(name) > 50:
        print("name must be a maximum of 50 characters long")
    else :
        print("name looks good")

    weight = float(input('weight: '))
    unit = input('(L)bs or (K)g: ')
    if unit.upper() == 'L':
        converted = weight * 0.45
        print(f"you are {converted} kilograms")
    elif unit.upper() == 'K':
        converted = weight / 0.45
        print(f"you are {converted} pounds")


def while_function():
    i = 1
    while i <= 5:
          print("x" * i)
          i = i + 1
    print("Done")

    secret_number = 9
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit :
        guess = int(input('Guess: '))
        guess_count += 1
        if guess == secret_number :
            print("correct guess you win!")
            break
    else:
        print("wrong guess you lose!")

    command = ""
    started = False
    while True:
           command = input("> ").lower()
           if command == "start" :
                if started :
                    print("The car has already started!")
                else :
                    started = True
                    print("The car has started")
           elif command == "stop" :
                if not started :
                    print("The car has already stopped!")
                else :
                    started = False
                    print("The car has stopped")
           elif command == "help" :
                print('''
    start = to start the car
    stop = to stop the car
    quit = to exit the program
                        ''')
           elif command == "quit" :
                break
           else :
                print("i don't understand that")


def for_function():
    prices = [10, 11, 12, 13, 14, 15]
    total = 0
    for price in prices:
           total += price
    print(f"total: ${total}")

    for x in range(5) :
        for y in range(5):
            print(f'{x} , {y}')

    numbers = [5,2,5,2,2]
    for item in numbers:
         print('x' * item)


    for x_count in numbers:
        output = ''
        for count in range(x_count):
            output += 'x'
        print(output)

    numbers = [1,2,3,4,5,6,7,8,9]
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    print (max)

    numbers = [2,2,3,6,8,0,6]
    duplicates = []
    for number in numbers:
        if number not in duplicates:
            duplicates.append(number)
    print(duplicates)


def dictionary_py():
    mouse = {
        "make":"dell",
        "age":2,
        "is 2.5ghz":"true"
    }
    print(mouse["make"])

    phone_number = input("phone: ")
    number = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
    }
    output = ""
    for ch in phone_number:
        output += number.get(ch, "!") + " "
    print(output)

    message = input(">")
    words = message.split(' ')
    emojis = {
        ":)":"😁",
        ":(":"😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    print(output)

def parameters_py(heading , head_ing):
    print(f"{heading} {head_ing}")
    print("Be a pro")

    parameters_py("python for beginners" , "new book")
    parameters_py("py for beginners" , "old book")


def parameters_py(heading , head_ing):
    print(f"{heading} {head_ing}")
    print("Be a pro")

    parameters_py(head_ing = "python for beginners" ,heading = "new book")
    parameters_py(head_ing = "py for beginners" , heading = "old book")


def returnstatement_py(number):
    return number * number


    print(returnstatement_py(3))


def emojis_converter(message):
    words = message.split(' ')
    emojis = {
        ":)":"😁",
        ":(":"😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


    message = input(">")
    print(emojis_converter(message))


def exceptions_py():
    try:
        age = int(input("age?"))
        income = 50000
        risk = income/age
        print(risk)
    except ZeroDivisionError:
        print("age cannot be zero")
    except ValueError:
        print("invalid value")


def modules_py():
    import utils

    numbers = [1,2,3,4,5,6,7,8]
    print(utils.findmax_py(numbers))


def random_py():
    import random

    for i in range(3):
        print(random.randint(10, 20))

    members = ['John' ,'Mary' ,'Bob' ,'Mosh' ,'Alice']
    leader = random.choice(members)
    print(leader)

#print(emojis_converter(":)"))
print(for_function())