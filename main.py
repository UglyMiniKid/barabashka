"""number1=int(input("Ведите число: "))
number2=0
number3=0
if number1%5==0:
    number2=1
if number1%3==0:
    number3=1
if number2==1 and number3==1:
    print("Число",number1,"делится на 3 и на 5 без остатка.")
elif number2==0 and number3==1:
    print("Число", number1, "делится на 3 без остатка, а на 5 нет.")
elif number2==1 and number3==0:
    print("Число", number1, "делится на 5 без остатка, а на 3 нет.")
else:
    print("Число",number1,"не делится на 3 и на 5 без остатка.")
number=int(input("Ведите число: "))
if number%5==0 and number%3==0:
    print("Импо")
n=int(input("Скока у тебя баллов, бездырь? "))
if n<=100 and n>=90:
    print("Отлично")
elif n<=69 and n>=50:
    print("Удовлетворительно")
elif n<=89 and n>=70:
    print("Хорошо")
else:
    print("Не удовлетворительно")
n1=int(input("Введите перваое число: "))
n2=int(input("Введите vtoroe число: "))
znak=input("Введите знак: ")
if znak=="+":
    print(n1+n2)
elif znak=="-":
    print(n1-n2)
elif znak=="*":
    print(n1*n2)
elif znak=="/":
    print(n1/n2)
else:
    print("Неверный знак")
a=int(input("Введите первую сторону: "))
b=int(input("Введите вторую сторону: "))
c=int(input("Введите третью сторону: "))
if a+b>c:
    print("Треугольник существует")
else:
    print("Треугольник не существует")
i=0
n=int(input("Ведите каличества звездачек: "))
for i in range(n):
    print("*"*i)
    i+=1
i=0
while i!=5:
    if i==0 or i==4:
        print("*****")
        i+=1
    elif i>0 and i<5:
        print("*"," ","*")
        i+=1
print("Всо, полый квадрат тута")

i=0
n=int(input("Укажити размер треугольнека: "))+1
while i!=n:
    print("*"*i)
    i+=1
print("Всо, треугальник гатоф")
i=0
n=int(input("Укажити размер треугольнека: "))+1
while i!=n:
    if i<=2 or i==n-1:
        print("*"*i)
        i+=1
    elif i>2 and i<=n-2:
        print("*"," "*(i-3),"*")
        i+=1
    elif i==n-1:
        print("*"*(i+3))
print("Рот шатал этого")
n=int(input("crjrf 'nb[ cfvs[ eltn& :"))
for i in range(0,n+1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
if i==n:
    for i in range(n-1,0,-1):
        for j in range(0,n-i):
            print(end=" ")
        for j in range(0,i):
            print("*",end=" ")
        print()
a = b = 1
lst = [a, b]
for i in range (2, 10):
    c = a+b
    lst += [c]
    a = b
    b = c
print(*lst)


from random import randint

minimum = int(input('Минимум: '))
maximus = int(input('Максимум: '))
elementi = int(input('Количество элементов: '))

lst = [randint(minimum, maximus) for i in range(elementi)]

s = set(lst)
for i in s:
    print(f"'{i}': {lst.count(i)}")
input_string=str(input("Строка"))
def count_vowels(input_string):
    vowels="аеёиоуюыэя"
    count=0
    for char in input_string.lower():
        if char in vowels:
            count+=1
print("Количество гласных:", count_vowels(input_string))
#задача 2
def rotate(input_string):
    words=input_string.split()
    rotated=words[::-1]
    return(rotated)
input_string=input("Введите строку: ")
result=rotate(input_string)
print(result)
#задачо номир 3
def find(input_string, search):
    if search in input_string:
        return"Есть такое"
    else:
        return"Нет такога"
print('ДА' if word in str.lower() else 'НЕТ')
user_input = str(input())
output = user_input.replace(' ','_')
print(output)
str = input('Введите строку: ')
word= input('Введите слово: ')


print('ДА' if word in str.lower() else 'НЕТ')
user_input = str(input())
output = user_input.replace(' ','_')
print(output)

user_input = input("Введите строку: ")

user_input = input("Введите строку: ")


if user_input == user_input[::-1]:
    print("ЭТА СТРОКА ПАЛИНДРОМ")
else:
    print ("ЭТА СТРОКА НЕ ЯВЛЯЕТСЯ ПАЛИНДРОМОМ")"""

str = input('Введите строку: ')
word= input('Введите слово: ')


print('ДА' if word in str.lower() else 'НЕТ')
user_input = str(input())
output = user_input.replace(' ','_')
print(output)

user_input = input("Введите строку: ")


if user_input == user_input[::-1]:
    print("ЭТА СТРОКА ПАЛИНДРОМ")
else:
    print ("ЭТА СТРОКА НЕ ЯВЛЯЕТСЯ ПАЛИНДРОМОМ")






