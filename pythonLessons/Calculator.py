print("Добро пожаловать в калькулятор!!")
try:a = int(input("Введите первое число "))
except ValueError:
    print("Введите число!")

print("Выберте действие: 1(+) 2(-) 3(/) 4(*)")
action = int(input())


try:b = int(input("Введите второе число "))
except ValueError:
    print("Введите число!")




if action == 1:
    result = a+b
    print("Ответ= " + str(result))


if action == 2:
    result = a-b
    print("Ответ= " + str(result))

if action == 3 :
    try: result = a/b
    except ZeroDivisionError:
        result = "На ноль делить нельзя"
    print("Ответ= " + str(result))


if action == 4:
    result = a*b
    print("Ответ= " + str(result))
