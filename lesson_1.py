# print("Hello world")
# """sdfsdf"""
# # true - 1
# # false - 0
# # # динамическася типизация
# # базовые типы данных
# # т.е типы данных могут менятся
# a = 2
# b = 1000000
# #print(a ** b)
# # x, y = int(input()), int(input())
# # res = (x + y) ** 23 - 5 + (5 / 7)
# # print(res)
#
# # 1
# print(17 / 2 * 3 + 2, 2 + 17 / 2 * 3, 19 % 4 + 15 / 2 * 3, 15 + 6 - 10 * 4, 17 / 2 % 2 * 3 ** 3)
# # ===========================
# # 2
# print((17 / 2) * (3 + 2), (2 + 17) / 2 * 3, 19 % (4 + 15) / 2 * 3, (15 + 6 - 10) * 4, 17 / 2 % (2 * 3) ** 3)
# # ===========================
# # 3
# money = 11
# bred = 1.50
# n = 3
# print(money - bred * n)
# # ==========================
# # 4
# ann = 2
# pole = 5
# print(pole, ann)
# # =========================
# # 5
# day = int(input())
# print(f"{day} суток = {day * 24} часов = {day * 24 * 60} минут = {day * 24 * 60 * 60} секунд")
# # ========================
# # 6
# dayy = 182
# print(dayy // 7)
# # ========================
# 7
#
# a, b = map(int, input().split())
# length = 30
# print(f"Можно отрезать {(a // length) * (b // length)} квадратов")
# # ========================
# # 8
# seconds = int(input())
# hours = seconds // 3600
# minutes = (seconds % 3600) // 60
# seconds -= hours * 3600 + minutes * 60
# print(f"{hours} час", f"{minutes} минут", f"{seconds} секунд", sep = "\n")
# # =========================
# # 9
# n = int(input())
# first = n // 100
# second = (n % 100) // 50
# ten = ((n % 100) // 10) % 5
# third = n % 10
# print(f"{first} купюры по 100 рублей", f"{second} купюры по 50 рублей", f"{ten} купюры по 10 рублей", f"{third} купюры по 1 рублей", sep = "\n")
# # =========================
# # 10
# h, up, down = int(input("Введите высоту шеста: ")), int(input("Введите на сколько метров поднимаетя улитка: ")), int(input("Введите на сколько метров улитка спускается: "))
# print((h - up - 1) // (up - down) + 2)
# # =========================
# # 11
# length = 56
# v, t, m = int(input("Введите скорость байкера: ")), int(input("Введите кол-во часов: ")), int(input("Введите кол-во минут: "))
# print(int((v / (t + m / 60)) % length))
#
#
# # ==============================
# # lesson 2
# # логические выражения
# # >, <, >=, <=
# # == проверяет на равентсво два оператораб проверяет по значению
# # is проверяет на область в памяти
# var1 = "hello"
# var2 = "Hello"
# print(id(var1), id(var2))
# print(var1 is var2)
# =================
# number = int(input())
# if number > 0:
#     # тело условного оператора
#     print("YES")
# elif number == 0:
#     print("NO")
#     print("ZERO")
# else:
#     pass
#
# season = input("Enter seson of the year: ")
# print(repr(season))
# if season == "winter":
#     print("winter is here")
# elif season == "autumn":
#     print("autumn")
# elif season == "spring":
#     print("spring")
# elif season == "summer":
#     print("summer")
# else:
#     print("Wrong answer")
# a, b, c = map(int, input().split())
# if a + b > c and b + c > a and a + c > b and a > 0 and b > 0 and c > 0:
#     if a == b == c:
#         print("Равносторонний")
#     elif a == b or a == c or b == c:
#         print("Равнобедренный")
#     elif a != b != c:
#         print("Разносторонний")
# else:
#     print("Не существует")
#    что написать if условие верно else что написать
# number = int(input())
# print("четное" if number % 2 == 0 else "нечетное")
# строки str это все, что в кавычках
# \a перенос курсора в начало строки, \t табуляция
# some_str = """
# fdafadf
# sdfsdfs
# """
# print(some_str.replace("\n", " "))
# name = "joHn watSon"
# name = name.lower()
# name = name.upper()
# name = name.capitalize()
# name = name.title()
# name = name.strip(" ")
# c = name. count("h")
# numb = name.find("o")
# print(repr(name))
# slice  (срез) str[start:end:step] str[sart:step] str[::step]
#
# name = "John Watson"
# print(name[1:4])
# print(name[3:0:-1])
# print(name[::2])
# print(name[::-1])
# print(name[:2] + name[5:8])
#
# name1 = "Jahn"
# name2 = "Pit"
# # print(name1 < name2)
# name = "Jahn Watson"
# str1 = name[:4]
# str2 = name[5:]
# print(str2 + " " + str1)
# str1 = "192.168.0.1"
# print(str1.replace(".", " "))
# print(int(str1[0:6]), int(str1[4:7]), int(str1[8]), int(str1[10]))
# # ===============================
# # 1
# number = int(input())
# if number % 10 == 3:
#     print("True")
# else:
#     print("False")
# # ===============================
# # 2
# a, b, c = map(int, input().split())
# if a < 0 or b < 0 or c < 0:
#     print("True")
# else:
#     print("False")
# # ===============================
# # 3
# n, k = map(int, input().split())
# if n % 2 == k % 2:
#     print("True")
# else:
#     print("False")
# # ===============================
# # 4
# x = int(input())
# if x % 3 == 0 and x % 10 == 5:
#     print("True")
# else:
#     print("False")
# # ===============================
# # 5
# a, b, c = map(int, input().split())
# k = 0
# if a % 2 == 0:
#     k += 1
# if b % 2 == 0:
#     k += 1
# if c % 2 == 0:
#     k += 1
# print(k)
# # ===============================
# # 6
# number = int(input())
# if (number // 10 + number % 10) // 10 != 0:
#     print("YES")
# else:
#     print("NO")
# # ===============================
# # 7
# number = int(input())
# first = abs(number) // 1000
# second = (abs(number) % 1000) // 100
# third = (abs(number) % 100) // 10
# fourth = (abs(number) % 10 )
# if first == second == third == fourth:
#     print("YES")
# else:
#     print("NO")
# # ===============================
# # 8
# year = int(input())
# if year % 4 == 0 and year % 100 != 0:
#     print("Високосный")
# else:
#     print("Не високосный")
#
# # ===============================
# # String tasks
# # 1
# s = input()
# print(s[2], s[-2], s[:5], s[:-2], s[2::2], s[1::2], s[::-1], s[::-2], len(s), sep="\n")
# # ===============================
# # 2
# word = input()
# if word[:1] == word[-1:]:
#     print("YES")
# else:
#     print("NO")
# # ===============================
# # 3
# word = input()
# print(word[1:4])
# # ===============================
# # 4
# word = "яблоко"
# print(word[1:5], word[-3:])
# # ===============================
# # 5
# s = "*"
# print(s * 5)
# # ===============================
# # 6
# s = input()
# n = len(s) // 2
# if s[:n] == s[:n:-1]:
#     print("YES")
# else:
#     print("NO")
# # ===============================
# # 7
# s = input()
# n = s.count("f")
# if n != 0:
#     if n == 1:
#         print(f"Index of letter f is {s.find('f')}")
#     else:
#         print(f"First in is  {s.find('f')},   Number of letters f is {n}")
# else:
#     print("ERROR!! There's NO letter f")
# # ===============================
# # 8
# s = input()
# n = s.count("f")
# if n != 0:
#     if n == 1:
#         print(-1)
#     else:
#         print(s.find("f", s.find("f") + 1))
# else:
#     print(2)
# # ===============================
# # 9
# s = input()
# print(s.replace("1", "one"))
# # ===============================
# # 10
# s = input()
# s = s.lower()
# g, c = s.count("g"), s.count("c")
# print(((g + c) * 100) / len(s))
# for цикл с параметром
# while цикл с условием
# # hometask 3
# # 1
# for i in range(20):
#     print("10")
# ============
# # 2
# a, b = map(int, input().split())
# for i in range(a, b + 1):
#     print(i)
# =============
# # 3
# n = int(input())
# for i in range(1, n + 1):
#     print(i ** 3, end = " ")
# ==================
# # 4
# for i in range(100, -101, -1):
#     print(i, end = " ")
# # 5
# a = int(input())
# for i in range(a, a ** 10 + 1):
#     if a % 2 == 0:
#         print(i)
# # 6
# sum = 0
# for i in range(100, 501):
#     sum += i
# print(sum)
# # 7
# c = 1
# for i in range(5, 21):
#     c *= i
# print(c)
# # 8
# n = int(input())
# c = 1
# for i in range(1, n + 1):
#     c *= i
# print((c))
# 10
# n = int(input())
# pre = 0
# nex = 1
# c = 1
# for i in range(n):
#     nex = c + pre
#     c = pre
#     pre = nex
#     print(nex, end = " ")
import shlex
import time

# # вывести все чилса от 1 до н с помощью while
# n = int(input())
# begin = 1
# while begin <= n:
#     print(begin, end = " ")
#     begin += 1
# дано число, вывести все его цифры
# n = int(input())
# n = str(n)
# n = n[::-1]
# n = int(n)
# while n != 0:
#     print(n % 10)
#     n //= 10
# # найти НОД двух чисел (наибольший общий делитель)
# a, b = map(int, input().split())
# numbers = 1
# c = True
# nod = 1
# while c:
#     if a % numbers == 0 and b % numbers == 0:
#         nod = numbers
#     numbers += 1
#     if numbers > a or numbers > b:
#         c = False
# print("NOD is ", nod)
# #  строка не изменяемая
# s = "hello"
# temp = ""
# print(id(s))
# for i in range(len(s)):
#     if i == len(s) - 2:
#         temp += s[i].upper()
#         continue
#     temp += s[i]
# print(temp)
# s = "hello world"
# gl = "aeyuioAEYUIO"
# temp = ""
# for i in range(len(s)):
#     if s[i] not in gl:
#         temp += s[i]
#
# print(temp)


#
# text = "dog   cat   frog   mouse   "
# temp = ""
# for i in range(len(text)):
#     if text[i] != " ":
#         temp += text[i]
#
#     elif temp:               # если строка существует, т.е она НЕ пустая
#         print(temp)
#         temp = ""
#
# text = "dog   cat   frog   mouse   "
# letter = "o"
# count = 0
# temp = ""
# for i in range(len(text)):
#     if text[i] != " ":
#         temp += text[i]
#
#     elif temp:            # если строка существует, т.е она НЕ пустая
#         if letter in temp:
#             count += 1
#             print(temp)
#         temp = ""
# print(count)

#
# lesson 5
# разбор 11 задачи на for
# взаимно простые числа - числа  с нод = 1 (4, 5) (12, 29) (15, 16)
# n, m = map(int, input("Enter n, m ").split())
# for numb in range(2, m + 1):
#     temp_numb = numb
#     temp_n = n
#     while temp_numb != 0 and temp_n != 0:
#         if temp_numb > temp_n:
#             temp_numb %= temp_n
#         else:
#             temp_n %= temp_numb
#     if temp_n + temp_numb == 1:
#         print(f"{numb} is simple with {n}")
# # 8
# number = int(input())
# min_num = number % 10
# while number:
#     if min_num > number % 10:
#         min_num = number % 10
#     print(min_num)
#     number //= 10
# !!!!!! tuple (кортежи) unmutable - неизменяемый !!!!!!
#          -5   -4   -3   -2   -1
#          0     1    2    3     4
# tup = ("hello", 94, True, 5.23, 94, (94, 94))
# tup2 = (1, 2, 3)
# tup += tup2
# print(tup.count((94, 94)))
# print(tup.index(94, 2))
# ВНИМАНИЕ СЮДА!!!!!!
# если написать tup = (5), то tup будет int, а не tupple, для этого надо написать запятую
# tup = (5,)
# print(type(tup))
# перебор
# for elem in tup:
#     print(elem)
# for ind in range(len(tup)):
#     print(tup[ind])
# задача на кортежи
# найти максимальный элемент
# tup = (5, 6, 1, 10, 18, 5, 2)
# max = tup[0]
# for i in tup:
#     if i > max:
#         max = i
#     print(max)
# !!!!!! list (списки) mutable - изменяемая структура !!!!!!
# lst = [5, 6, 5, 2.42, "hello", True, (6, 1, 2), [5, 2, 9]]
# tup = (5, 6, 2.42, "hello", True, (6, 1, 2), [5, 2, 9])
# print(lst.__sizeof__())
# print(tup.__sizeof__())
# lst += [5, 2, 6]
# lst.append(5) добавление в конец
# lst.insert(1, 5) добавление в определеную позицию
# lst.remove(5)
# while 5 in lst:
#     lst.remove(5)
# lst.pop(10)
# if 15 in lst:
#     lst.remove(15)
# del lst[3:5] // del может удалять последовательность элементов
# lst.extend([5, 2, 5])// распаковка списка, кортежа или же строки, просто число добавлять нельзя
# lst2 = lst так делать нельзя
# lst2 = lst.copy() вот так надо
# s = "hello"
# lst = list(s)
# print(lst)
# lst = []
# n = int(input("Enter count of element: "))
# for i in range(n):
#     element = int(input("Enter element: "))
#     lst.append(element)
# print(lst)
# list comprehension генератор списков
# 1 [что хотим добавить  for  из чего хотим добавить   in   итерабельный объект ]
# print([numb.upper() for numb in "hello"])
# print(list("hello"))
# print([numb ** 3 for numb in range(1, 11)])
# 2 [что хотим добавить  for  из чего хотим добавить   in   итерабельный объект if условие верно]
# print([numb for numb in range(1, 11) if numb ** 2 % 3 == 0 ])
# print([symb for symb in "Hello" if symb in "aeyuioAEYUIO" ])
# 3 [что хотим добавить if условие верно else что хотим добавить for  из чего хотим добавить   in   итерабельный объект ]
# тернарный оператор print(("четное" if 4 % 2 == 0 else "нечетное"))
# print([numb if numb % 2 == 0 else numb ** 2 for numb in range(1, 11) ])

# print([int(input()) for i in range(5)])
# print([int(i) for i in input().split()]) // ввод по разделителю, т.е в данном случае по пробеу

# удаление слов, которые начинаются с большой буквы
# s = "hello world i am Piter Parker"
# s = "        "
# print(s.up)
# lst = list(s.split())
# lst = [elem for elem in lst if elem[0].islower()]
# s = " ".join(lst)
# print(s)
# # 9 taska with cows
# n = int(input())
# for i in range(1, n + 1):
#     if i % 100 in [11, 12, 13, 14]:
#         print(f"На лугу {i} коров")
#     elif i % 10 == 1:
#         print(f"На лугу {i} корова")
#     elif i % 10 in [2, 3, 4]:
#         print(f"На лугу {i} коровы")
#     else:
#         print(f"На лугу {i} коров")
# hometask 4
# # 1
# n = int(input())
# k = 1
# while k <= n:
#     print(k)
#     k += 1
# # 2
# n = int(input())
# b = 0
# sum = 0
# while b <= n:
#     if b % 2 == 0:
#         sum += b
#     b += 1
# print(sum)
# # 3
# n = int(input())
# b = 1
# p = 1
# while n != 0:
#     if (n % 10) % 2 == 0 and n % 10 != 0:
#         p *= (n % 10)
#     n //= 10
# print(p)
# # 4
# n = int(input())
# b = 1
# while True:
#     if b ** 2 < n:
#         print(b ** 2)
#         b += 1
#     else:
#         break
# # 5
# n = int(input())
# b = 1
# while True:
#     if b ** 2 > n:
#         print(b ** 2)
#         break
#     else:
#         b += 1
# # 6
# n = abs(int(input()))
# while True:
#     if n // 10 == 0:
#         print(n)
#         break
#     else:
#         n //= 10
# # 7
# n = abs(int(input()))
# sum = 0
# while True:
#     if n != 0:
#         sum += n % 10
#         n //= 10
#     else:
#         break
# print(sum)
#
# # 8
# n = abs(int(input()))
# min = 9
# while n != 0:
#     if min > n % 10:
#         min = n % 10
#     n //= 10
# print(min)
#
# tasks str
# # 1
# s = input()
# t = ""
# for i in range(len(s)):
#     if s[i] == "z":
#         t += s[i] + "!"
#     else:
#         t += s[i]
# print(t)
# 2
# s = input()
# p = ""
# for i in range(len(s)):
#     if s[i] not in p:
#         p += s[i]
# print(p)
# # 3
# s = input()
# n = ""
# c = 0
# for i in range(len(s) - 1):
#     if s[i] == "b" and s[i + 1].isdigit():
#         continue
#     else:
#         n += s[i]
# n += s[-1]
# print(n)
# 3.1
# s = input()
# n = ""
# c = 0
# for i in range(len(s) - 1):
#     if s[i].isalpha() and s[i].islower():
#         continue
#     else:
#         n += s[i]
# if not(s[-1].isalpha() and s[-1].islower()):
#     n += s[-1]
# print(n)
# 4
# s = input()
# c = 0
# for i in reversed(range(len(s))):
#     if s[i] == " " and s[i - 1] == "k":
#         c += 1
# if s[-1] == "k":
#     c += 1
# print(c)
# 5
# s = input()
# ans = ""
# count = 1
# for i in range(len(s) - 1):
#     if s[i] == s[i + 1]:
#         count += 1
#     else:
#         ans += s[i] + str(count)
#         count = 1
# ans += s[-1] + str(count)
# print(ans)
#
#
#
# hometask 5
# 1
# sum = 0
# t = (6, 2, 3, 4, 5, 7, 8, 9, 10, 28, 496, 8128, 33550336, 12, 26)
# for i in range(len(t)):
#     for j in range(1, t[i]):
#         if t[i] % j == 0:
#             sum += j
#         if t[i] == sum:
#             print(t[i])
#             break
#     sum = 0
# 2
# t = (6, 3, 7, 4, 5, 2, 8, -20, 9, 10, 28, -30, 496, 8128, 12, 26)
# min = t[0]
# max = t[0]
# for i in range(len(t)):
#     if max < t[i]:
#         max = t[i]
#     if min > t[i]:
#         min = t[i]
# print(max - min, max, min)
# # # 3
# t = (5, 2, -2, 7, -8, 0, -9, 1, )
# count = 0
# for i in range(len(t) - 1):
#     if t[i] >= 0 and t[i + 1] < 0:
#         count += 1
#     elif t[i] <= 0 and t[i + 1] > 0:
#         count += 1
# if t[-2] >= 0 and t[-1] <= 0:
#     count += 1
# elif t[-2] <= 0 and t[-1] >= 0:
#     count += 1
# print(count)
# это(ниже) решение 3й задачи но только через вложенный цикл, что оч сложно
# for i in range(len(t)):
#     for j in range(len(t)):
#         if t[i] / abs(t[j]) == -1:
#             count += 1
# print(count)
# 4
# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 79, 191)
# count = 0
# for i in range(len(t)):
#     for j in range(1, t[i] + 1):
#         if t[i] % j == 0:
#             count += 1
#     if count == 2:
#         print(t[i])
#     count = 0
# # 5
# t = (5, 2, 6, 8, 9, 7, 5, 7, 8, -1, -2, -3, -4, 1, 2, 3, 4)
# maxcount_second = ()
# maxcount_one = ()
# count_one = 0
# count_second = 0
# for i in range(len(t) - 1):
#     if t[i] > t[i + 1]:
#         count_one += 1
#         maxcount_one += (count_one,)
#     else:
#         count_one = 0
#     if t[i] < t[i + 1]:
#         count_second += 1
#         maxcount_second += (count_second, )
#     else:
#         count_second = 0
# maxfirst = max(maxcount_one)
# maxsecond = max(maxcount_second)
# print(maxfirst, maxsecond)
# if maxfirst > maxsecond:
#     print(f"Последовательность убывающая {maxfirst}")
# elif maxfirst == maxsecond:
#     print(f"Две одинаковых по длине последовательности")
# else:
#     print(f"Последовательность возрастающая {maxsecond}")
# # 6
# t = (1, 2, 4, 1, 2, 6, 3, 4, 5, 6, 0, 2, -1, 10, -2, -1, 0)
# for i in range(len(t)):
#     for j in range(i + 1, len(t)):
#         if t[i] == t[j]:
#             print(t[i], end=" ")
#
# # 7
# lst = [5, 6, 7, 8, 9, 10, -10, 0, -1, 2, 4]
# for i in lst:
#     if i % 2 == 0 and i != 0:
#         print(i, end=" ")
# # 8
# lst_first = [1, 2, 3, 4, 5, 6, 7]
# lst_second = [-1, 0, 2, 9, 10, 28, 14, 3, 6]
# lst_ans = []
# for i in lst_first:
#     if i in lst_second:
#         lst_ans.append(i)
# print(min(lst_ans))
# # 9
# count = 0
# lst = [2, 5, 6, 7, 2, 8, 1, 9, 3]
# for i in range(len(lst) - 1):
#     if lst[i] > lst[i + 1]:
#         count += 1
# print(count)
# 10
# n = 0
# lst = [18, 89, 122, 3452]
# i = 0
# while i < len(lst):
#     if lst[i] % 2 == 0:
#         lst.insert(i + 1, int((str(lst[i]))[::-1]))
#     i += 1
# print(lst)
# # 11
# lst = [5, 2, 4, 5, 1, 2]
# lst_ans = []
# for i in range(len(lst)):
#     if lst[i] not in lst_ans:
#         count = lst.count(lst[i])
#         print(f"{lst[i]} - {count}", end=" ")
#         lst_ans.append(lst[i])
# # 12
# lst = [-1, 2, 0, 8, -7, 8, -10, 7]
# i = 0
# k = len(lst)
# while i < k:
#     if lst[i] <= 0:
#         lst.append(lst[i])
#         lst.remove(lst[i])
#         k -= 1
#     else:
#         i += 1
# print(lst)
# # 13
# lst = [1, 2, 0, 3, 4, 2, 8, 7, 1, 9, -1, 11]
# count = 0
# i = 0
# while i < len(lst):
#     count = lst.count(lst[i])
#     if count == 1:
#         lst.insert(i + 1, lst[i])
#     else:
#         i += 1
# print(lst)
# 10, 11, 12 надо через while решать ибо мы не знаем кол-во итераций
# SOLID надо чекнуть
# метаклассы
# bootssnipp - сайт с сайтами с открытым кодом
# lesson 6
# s = "sfdsdfgdfgk sdfsdfasdf adsf dfsak asdfdk"
# lst = s.split()
# print(len([elem for elem in lst if elem[-1] == "k"]))
# lst = [1, 1, 1, 1, 1]
# print(lst)
# count = 1
# lst2 = []
# i = 0
# while i < len(lst):
#     if lst[i] < lst[i + 1]:
#         count += 1
#     i += 1
# print(count)
# count = 0
# number = int(input())
# sum = 0
# while number != 0:
#     number += number
#     count += 1
#     number = int(input())
#     if number > 10:
#         break
# else:
#     print("break не исполнился")
#     print(count)
# print(sum)
# print(count)
# множества - коллекция изменяема и frozenset - замороженнное множество, т.е неизменяемая коллекция
# set1 = set() # пустое множество просто написать set1 = {} нельзя
# print(type(set1))
# внутри множества могут быть только неизменяемые типы
# set_1 = {5, 5, 2, 2, 4, "hello"}
# for elem in set_1:
#     print(elem)
# set_1.update({1, 2, 3, 4})
# print(set_1)
# set_1.discard(5)
# if 5 in set_1:
#     set_1.remove(5)
# print(set_1)
# set_1 = {1, 2, 6, 7, 9}
# set_2 = {2, 3, 6, 7, 11}
# print(set_1.union(set_2))
# print(set_1)
# # print(set_1.intersection_update(set_2))# если хотим обновить, т.е запписать изменения в сет, надо юзать update
# print(set_1)
# # print(set_2.difference(set_1))
# print(set_1)
# print(set_1.symmetric_difference(set_2))
# print(set_1)
# print(set_1.issubset(set_2))
# print(set_2.issuperset(set_1))#подмножества, все чекать в таблице, которую скинул Денис
# set_1 = {4, 2, 1, 5}
# f_set1 = frozenset(set_1)
# print(f_set1)
# Даны два списка найти то, что не содержится одновременно в 1 и 2\
# lst = [5, 2, 6, 1, 2, 5, 2]
# lst_2 = [5, 2, 5, 1, 2, 9]
# set1 = set(lst)
# set2 = set(lst_2)
# print(set1 ^ set2)# ^ этоот значок это symetricdifference
# print(set1.symmetric_difference(set2))
# словари  dict(key : value) - изменяемая коллекция ассоциативный массив
# friends_phones = {"Vasya":37542611, "Anna":556165321, "Pavel":546516}# первый аргумент это ключ, второе значение
# key is uniq ключи уникальны
# key is unmutable ключи неизменямые (str, float, bool, tuple, int)
# value - любой тип данных, могут повтаряться
# for key in friends_phones:
#     print(key, friends_phones[key])
# for friend,phone in friends_phones.items():
#     print(friend, phone)
# for phone in friends_phones.values():
#     print(phone)
# friends_phones["Angelina"] = 45624516
# print(friends_phones)
# friends_phones.update({"Paul": 56465161, "Gena":3214101 })
# print(friends_phones)
# friends_phones.pop("Vasya")
# print(friends_phones)
# hometask 6
# # 1
# lst = list(map(int, input().split(" ")))
# sett_first = set()
# for i in range(len(lst)):
#     if lst[i] in sett_first:
#         print(lst[i], "YES")
#     else:
#         print(lst[i], "NO")
#         sett_first.add(lst[i])
#
#
# # 2
# first = set()
# ans = set()
# number = 0
# number = int(input("Enter correct value: "))
# ans = set(map(int, input().split(" ")))
# if number in ans:
#     print("YES")
# else:
#     print("NO")
# while True:
#     str = input()
#     if str == ".":
#         break
#     first = set(map(int, str.split(" ")))
#     if number in first:
#         print("YES")
#         ans = ans & first
#     else:
#         print("NO")
# print(ans)
#
# # 3
# school = {"9A": 30, "9B": 25, "9C": 31, "9G": 29}
# school["9A"] = 34
# school.update({"9F": 39})
# school.pop("9A")
# sum = 0
# for key in school:
#     sum += school[key]
# print(sum)
#
#
# # 4
# str = input()
# dct = {}
# while str[-1] != ".":
#     key = str[:str.find("–") - 1]
#     value = str[str.find("–") + 2:]
#     dct.update({key: value})
#     str = input()
# m = int(input())
# lst = []
# for i in range(m):
#     lst.append(input())
# for i in range(len(lst)):
#     if lst[i] in dct:
#         print(dct.get(lst[i]))
#     else:
#         print("Не найдено")
#
#
# # 5
# dct = {}
# str = input()
# while str[-1] != ".":
#     if (str.isalpha()):
#         if dct.get(str) == None:
#             print("Пользователь не найден")
#         else:
#             print(dct.get(str))
#     else:
#         key = str[:str.find(" ")]
#         value = str[str.find(" ") + 1:]
#         dct[key] = value
#     str = input()
#
# dopy
# # 1
# lst = [7, 4, 1]
# i = 0
# k = len(lst)
# while i < k:
#     lst.insert(i + 1, 0)
#     i += 2
# print(lst)
#
#
#
# # 2
# n = int(input())
# i = 0
# k = 1
# while i <= (n - i) + 1:
#     for j in range(1, i + 1):
#         if ((n - i) + 1) - i == 0:
#             print(i, end=" ")
#             break
#         else:
#             print(i, end=" ")
#     i += 1
#
#
# # 3
# from random import randint
# sum = 0
# n, m = map(int, input("Enter the number of rows and column: ").split())
# matrix = [[randint(1, 10) for j in range(m)] for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         if i + j == n - 1:
#             sum += matrix[i][j]
# print(matrix)
# print(sum)
#
#
# # 4
# lst = [4, 8, 0, 3, 4, 2, 0, 3, 9]
# lst_second = []
# for i in range(len(lst)):
#     if lst.count(lst[i]) > 1:
#         if lst[i] in lst_second:
#             continue
#         else:
#             lst_second.append(lst[i])
# print(lst_second)
#
#
# #  5
# matrix = []
# row, column = map(int, input().split(" "))
# for i in range(1, row + 1):
#     a = []
#     for j in range(1, column + 1):
#         a.append(j ** i)
#     matrix.append(a)
# for i in range(row):
#     for j in range(column):
#         print(matrix[i][j], end=" ")
#     print()
#
#
# # 6 как сделать ввод не по одной цифре в строке, а по n цифер
# n = int(input())
# matrix = []
# str = ""
# for i in range(n):
#     a = []
#     for j in range(n):
#         a.append(input())
#     matrix.append(a)
# for i in range(n):
#     str = ""
#     for j in range(n):
#         str += matrix[i][j]
#     if str == str[::-1]:
#         print(str, "YES")
#     else:
#         print(str, "NO")
#
#
# # 7
# n = int(input())
# matrix = []
# for i in range(n):
#     a = []
#     for j in range(n):
#         if i - j == 0:
#             a.append(0)
#         else:
#             a.append(abs(i - j))
#     matrix.append(a)
# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j], end=" ")
#     print()


# # wargaming A
# n, k = map(int, input().split(" "))
# lst_ans = []
# for i in range(2, k):
#     if k % i == 0:
#         lst_ans.append(i)
#         print(i)
# count = 0
# for i in range(len(lst_ans)):
#     if lst_ans[i] <= n and n // lst_ans[i] <= n and k % lst_ans[i] == 0:
#             count += 1
# print(count)


# # wargaming B
# n = int(input())
# cost = list(map(int, input().split(" ")))
# if len(cost) != 9:
#     print("ERROR!!")
# i = len(cost) - 1
# while i != -1:
#     print(cost[i])
#     i -= 1
# DRY - Don't repeat yourself
# KISS - Keep It Simple Stupid


# functions
# global mainspace  мы пишем все в глобал мэинспэйс
# def show_lst():
#     lst = [1, 2, 3, 4, 5, 6]
#     for i in lst:
#         print(i)

# def registr(password: str, name, age):
#     print(f"Greeting {name} {age} {password}")
# registr(password=[1, 2, 3], age=25, name="Oleg")
# # анотация это: password: str
# n = int(input())
# stek = []
# while n != -1:
#     stek.append(n)
#     n = int(input())
# for i in reversed(stek):
#     print(i)

# l1 = list(map(int, input().split()))
# l2 = list(map(int, input().split()))
# def leetcode(l1, l2):
#     str1 = ""
#     str2 = ""
#     ansList = []
#     for i in l1:
#         str1 += str(i)
#     for i in l2:
#         str2 += str(i)
#     ans = int(str1) + int(str2)
#     for i in str(ans)[::-1]:
#         ansList.append(int(i))
#     return(ansList)
# print(leetcode(l1, l2))
# lesson 8(may be)
# def greeting():
#     # если функция ничего не возвращает, то она называется процедурой
#     print("Hello world")
# greeting()
# global scope
# def greeting(name: str, age: int):
# local scope
#     print(f"Hello {name} age {age}")
# greeting("John", 28)
# unmutable(неизменяемые) переменные передаются по значению !!!!
# mutable(изменяемый) в функцию передается по ссылке!!!!
# balance=5600 - ключевой аргумент
# args, kwargs!!!1!!!
# *args - позиционнные аргументы
# чтобы принимать словари(ключ: значение) придумали **kwargs key word arguments
# образец def(date, *args, balance, balanceMany=5615, **kwars):
# def workers(*args, balance, balanceMany = 999999, **kwargs):
#     print(args)
#     print(balance)
#     print(kwargs)
#     for i in kwargs:
#         print(kwargs[i])
#     print(balanceMany)
# workers("Vasya", "Petya", "Anna", balance=56000, balanceMany=100, balance1=9800, balance4=1516)
# # самое популярное, самый популярный прием аргументов
# def fun(*args, **kwargs):
#
# ================
# анонимная функция
# fun = lambda x=1,y=2: x + y
# print(fun())
# def chet(number):
#     return not number % 2
# lst = [5, 2, 6, 1, 7, 8]
# lst.sort(key= lambda numb: not numb % 2)
# print(lst)
# lst.sort(key= chet)
# print(lst)
# =========
# kr = lambda x: "YES" if x % 3 == 0 else "NO"
# print(kr(5))
# lst = [1, 6, 8, 2, 7]
# lst = ["John", "Mary", "Jack", "William"]
# lst.sort(key=len)
# print(lst)
# =========
# map
# lst = [5, 2, 5, 7, 1, 2]
# balance = {"John": 234, "Mark": 199, "Ann": 120}
# for name in map(lambda *name: (balance[name] + 20) if balance < 200 else balance[name], balance):
#     print(name, balance[name])
# function filer
# lst = [5, 2, 5, 7, 1, 2]
# lst_2 = list(filter(lambda x: not x % 2, lst))
# print(lst_2)
# =========
# words = ["hello", "word", "price", "gold"]
# words2 = list(filter(lambda elem: len([sym for sym in elem if sym in "aeyio"]) == 2, words))
# print(words2)
# ======================
# x = 2
# def fun():
#     global x
#     x += 3
#     print(x)
# fun()
# ==============
# декораторы
# bgel
# global
# local
# enclosing
# built-in
# def fun(number):
#     def wrapper():
#         nonlocal number
#         number += 1
#         print(number)
#     wrapper()
# fun(42)

# замыкание clasure
# т.е мы можем запоминать некий результат(мы запомнили, т.е замкнули)
# def person(name):
#     def wrapper():
#         print(name.capitalize())
#     return wrapper
#
# p = (person("Vova"))
# p()
# ==========

# def counter(x):
#     def wrapper(a):
#         nonlocal x
#         x += a
#         print(x)
#     return wrapper
# c = counter(0)
# c(1)
# ===========

# декоратор - это функция, которая принимает функцию, ее модернизирует и возвращает


# def decorator(fun):
#     def wrapper(name: str):
#         if name.capitalize() == name:
#             fun(name)
#             return fun(name)
#         else:
#             return "Hello " + name.capitalize()
#     return wrapper
#
# @decorator
# def greeting(name: str):
#     return "Hello " + name
#
#
# decorSay = decorator(greeting)
# print(decorSay("peter"))


# примеры
# users = {"John": 1234, "Jack": 590, "Anna": 900}
# def balance(**kwargs):
#     for name, price in kwargs.items():
#         if price < 1000:
#             kwargs[name] += 100
#     return kwargs
# users = balance(**users)
# print(users)
#
# def add(a,b):
#
#     return a + b
#
# def function(func):
#     count = 0
#
#     def wrapper(a, b):
#         nonlocal count
#         count += 1
#         print(func(a, b))
#         return count
#
#     return wrapper
#
# w = function(add)
# print(w(5, 6),"\n","============")
# print(w(8, 1),"\n","============")
# print(w(21, 6),"\n","============")
# print(w(5, 35),"\n","============")
# print(w(223, 6),"\n","============")
# print(w(5, 8941),"\n","============")


# stepik
# def print_given(*args, **kwargs):
#     for i in args:
#         print(i, type(i))
#
#     kwargs = dict(sorted(kwargs.items(), key = lambda item: item[1]))
#     for key in kwargs:
#         print(key, kwargs[key], type(kwargs[key]))
#
#
# print_given(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two = 2, one = 1, three = 3)
#

# Hometask 8
# 1
# n = int(input())
#
# def fib(n):
#     fib1 = 0
#     fib2 = 1
#     for i in range(n - 1):
#         fib1, fib2 = fib2, fib1 + fib2
#     return fib2
#
# def factorial(n):
#     tmp = 1
#     for i in range(1, n + 1):
#         tmp *= i
#     return tmp
#
#
# print(fib(n) + factorial(n))
# ====================
# # 2
#
# def closet_mod_5(x):
#     i = 0
#     y = x
#     while i != -1:
#         if y >= x and y % 5 == 0:
#             i = -1
#             return y
#         else:
#             i += 1
#             y += 1
#
# print(closet_mod_5(6))
# =================
# # 3
# #
# v = input()
#
# def check_variable(v):
#     if v[0] == "_" or v[0].isalpha():
#         print("Можно использовать")
#     else:
#         print("Нельзя использовать")
# # Поработали, и хватит
# while v != "Поработали, и хватит":
#     check_variable(v)
#     v = input()
#
# ===========
# # 4
# money, years = map(int, input().split())
#
# def bank(money, years):
#     for i in range(years):
#         money += 0.1 * money
#     return money
#
# print(bank(money, years))
#
# ================
# # 5
# import timeit
#
# def decorator(func):
#     def wrapper(n):
#         start = time.time()
#         func(n)
#         return time.time() - start
#     return wrapper
#
# @decorator
# def numb(n):
#     count = 0
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 count += 1
#         if count == 2:
#             print(i)
#         count = 0
#
# print(numb(100))
#
#
# # 6
# import timeit
# def decorator(func):
#     def wrapper():
#         start = time.time()
#         func()
#         return time.time() - start
#     return wrapper
#
# @decorator
# def registration():
#     login = input()
#     password = input()
#
# print(registration())


# import vk_api
# import time
# import datetime
#
# token = "vk1.a.60XH_sgQCbjgteP6x44DGMuUBrfwqeI8dg6GHTdCAn3v0a40owhG9B-U4m7dLDvC825ERc2c2cxo_IT4LsjgM_aDNZ2I2w6Y4m1rMTc4gw36r3BxCn4hRzTL3mTfUihdvuoDntIL1_nNxXiT6U_3pB4fJtYGaW9Jq-INWuOk-GwtcfEZLlOP4cRBVGwB59NoaZjISxG5jtye1k-aNQs65A&expires_in=0"
#
#
# vk = vk_api.VkApi(token=token)
#
#
# try:
#     vk.auth()
# except vk_api.AuthError as error_msg:
#     print(error_msg)
#     exit()
#
#
# def send_message(user_id, message):
#     vk.method("messages.send", {"user_id": user_id, "message": message})
#
#
# send_time = datetime.datetime(2023, 2, 21, 1, 20, 0)
#
#
# now = datetime.datetime.now()
#
#
# delta = (send_time - now).total_seconds()
#
#
# time.sleep(delta)
#
#
# send_message(user_id=175163337, message="Привет, это автоматически отправленное сообщение!")
#
# print("Сообщение успешно отправлено!")


# args = map(int, input().split())
#
#
# for i in args:
#     print(float(i))

# number_names = {
#         0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
#         10: 'ten', 11: 'eleven', 12: 'twelve',
#         13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}
#
# lst = list(map(int, input().split()))
#
# lst = sorted(lst, key=lambda i: number_names[i])
# for i in range(len(lst)):
#     print(lst[i], end=" ")
#
#
# def composition(f, g):
#     ans1 = g
#     def h(*args):
#         return f(ans1(*args))
#     return h
#
# h = composition(lambda x: x**2, lambda x: x + 1)
# print(h(5))
#
# h = composition(lambda x: x, composition(lambda x: x**2, lambda x: x + 1))
# print(h(5))
#
# h = composition(sum, lambda x, y, z: (x**2, y**3, z**4))
# print(h(2, 3, 9))


# def introdecer(func):
#     def wrapper(*args, **kwargs):
#         print(__name__.func)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @introdecer
# def gectter(*args, **kwargs):
#     for i in range(len(args)):
#         print(args[i])
#
# gectter(1,8,9,0,5)

# #
# def flip(func):
#
#     def wrapper(*args, **kwargs):
#         args = args[::-1]
#         return func(*args,**kwargs)
#     return wrapper
#
# @flip
# def div(x, y, show=False):
#     res = x / y
#     if show:
#         print(res)
#     return res
#
#
# div(2, 4, show=True)



# def findMedianSortedArrays(nums1, nums2):
#     # Ensure that nums1 is the smaller array
#     if len(nums1) > len(nums2):
#         nums1, nums2 = nums2, nums1
#
#     m, n = len(nums1), len(nums2)
#     start, end = 0, m
#
#     while start <= end:
#         i = (start + end) // 2
#         j = (m + n + 1) // 2 - i
#
#         # Check if we have found the correct i
#         if i > 0 and nums1[i - 1] > nums2[j]:
#             end = i - 1
#         elif i < m and nums2[j - 1] > nums1[i]:
#             start = i + 1
#         else:
#             # We have found the correct i
#             if i == 0:
#                 max_of_left = nums2[j - 1]
#             elif j == 0:
#                 max_of_left = nums1[i - 1]
#             else:
#                 max_of_left = max(nums1[i - 1], nums2[j - 1])
#
#             if (m + n) % 2 == 1:
#                 return max_of_left
#
#             if i == m:
#                 min_of_right = nums2[j]
#             elif j == n:
#                 min_of_right = nums1[i]
#             else:
#                 min_of_right = min(nums1[i], nums2[j])
#
#             return (max_of_left + min_of_right) / 2
#
#
# print(findMedianSortedArrays([1,3], [2]))

# new lesson Files
# Режимы доступа
# w - write(запись, все что было, то пропадает(стирается)...) - режим по-умолчанию
# r - read чтение(считываем все из файла)
# a - append дозапись(записывает в конец файла)
# x - запишет информацию в файл если файла не существует(или он пуст)
# комбинированные режимы доступа
# w+ r+ a+ wb ab rb xb+ wb+ ab+ rb+ xb+
# file = open("test_file.txt", "r", encoding="UTF-8")
# students = {}
# for line in file:
#     lst = line.rstrip().split()
#     marks = list(map(int, lst[1:]))
#     students[lst[0]] =  marks
#
# file.close()
# print(students)
# file_avg = open("avg_marks", "w", encoding="UTF-8")
# for name, marks in students.items():
#     file_avg.write(name + " " + str(sum(marks) / 5) + "\n")
# file_avg.close()
# lst = some_str.replace("\n", " ").rstrip().split()
# lst = list(map(int,lst))
# print(lst)


# что такое контекстный менеджер??
# enter - вход - позволяющий получить вход
# exit(выход)
# with open("test_file.txt", "r", encoding="UTF-8") as file:
#     s = file.read()
#     print(s)
# print("hello")

# Решение задачи
# with open("test_file.txt", "r", encoding="UTF-8") as file:
#     lst = []
#     for line in file:
#         lst.append(line.rstrip())
#
#     print(lst)
# max_len = 0
# number = 1
# for id, line in enumerate(lst):
#     if len(line) > max_len:
#         max_len = len(line)
#         s = line
#         number = id + 1
# print(s)
# print(max_len)
# print(number)
# =============
# with open("test_file.txt", "r", encoding="UTF-8") as file:
#     lst = []
#     for line in file:
#         lst.extend(line.rstrip().split())
# ============
# csv(comma separated values) file значения разделенные запятой
# import random
# import csv
# lst = [str(random.randint(1, 10)) for i in range(100)]
# print(lst)
# # print(",".join(lst))
# # with open("test_csv.csv", "w") as file_csv:
# #     file_csv.write(",".join(lst))
# with open("test_csv.csv", "w") as file:
#     s = csv.reader(file, delimiter=";")
#     print(s)
#     for i in s:
#         print(i)


# # json
# import json
# person = {
#     "name": "John",
#     "lastname": "Watson",
#     "age": 24
# }
# # dumps - стерелизует объект(перевод объекта из лубого типа данных в строку)
# print(json.dumps([42, 2,2,8]))
# with open("test_json.json", "w", encoding="utf-8") as file_json:
#     json.dump(person, file_json, indent=4)
# with open("test_json.json", "r", encoding="utf-8") as file_json_read:
#     person_2 = json.load(file_json_read)
# print(person_2)
