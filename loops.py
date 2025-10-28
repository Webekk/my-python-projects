# Exercise 1: Print first 10 natural numbers using while loop

# for i in range(1,11):
#     print(i)


# Exercise 2: Print the following pattern
"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

"""
# print()
# rows = 5
# for i in range(1,rows + 1):
#     for j in range(1, i + 1):
#         print(i, end="")
#     print("")
#
# for i in range(1,rows + 1, 1):
#     for j in range(1, i + 1):
#         print(j , end="")
#     print("")


# Exercise 3: Calculate sum of all numbers from 1 to a given number

# s = 0
# n = int(input("Input the number that you want to see the sum of: "))
#
# for i in range(1, n + 1):
#     s += i
# print("\n")
# print(s)


# Exercise 4: Print multiplication table of a given number

# print("Multiplication table")
# variable = int(input("Print multiplication table: "))
# for i in range(1,10 + 1):
#     p = variable * i
#     print(p)

# Exercise 5: Display numbers from a list using a loop  number % 5 == 0

# numbers = [12, 75, 150, 180, 145, 525, 50]
#
# for number in numbers:
#     if number > 500:
#         break
#     elif number > 150:
#         continue
#     elif number % 5 == 0:
#         print(number)


# Exercise 6: Count the total number of digits in a number

# count = 0
# number = 74532
#
# while number != 0:
#     number = number // 10
#     count += 1
# print(count)
#
#
# for i in range(5):
#     print(i)
# print("Done")


# Exercise 7: Find prime numbers in range()

# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True
#
# firstRangeNumber = 1000
# secondRangeNumber = 9999
# primes = []
#
# for i in range(firstRangeNumber, secondRangeNumber + 1):
#     if is_prime(i):
#         primes.append(i)
# print(primes)


# Exercise 12: Display Fibonacci series up to 10 terms

# Podejście iteracyjne, funkcja po kolei sprawdza pierwsze parametry tzn 0 i 1 i pozniej przechodzi przez loop,
# pętla zaczyna sie od 3 elementu [2] i dodaje sasiednie ze soba wartosci ktore zostaly zapisane w liscie
# pod koniec operacji dodawania, dodaje uzyskana wartosc do list fib_series

def fibonacci_iterative(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_series = [0, 1]

    for i in range(2, n):
        next_number = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_number)
    return fib_series

print(fibonacci_iterative(100))

# Podejście rekurencyjne, (funkcja odwołuje sie do samej siebie), najpierw sprawdza podstawowe conditions
# n < = 0 i n == 1 a na koniec zwraca dalsze odwołania do funkcji tutaj juz w głownym programie mamy ustalona
# wartosc dla zmiennej n jakos 10, tworzymy liste i w srodku listy uzywamy list comprehension z nasza funkcja przeiterowana
# przez n razy, na koniec wyświetla wynik
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = 10
fibonacci_sequence = [fibonacci_recursive(i) for i in range(n)]

for item in fibonacci_sequence:
    if item % 2 == 0:
        print(item)
    else :
        continue

def przyjmij_liste_liczb(liczba):
    return max(liczba)

numbers = [1,2,3,4,5]

najwieksza_liczba = przyjmij_liste_liczb(numbers)
print("Największa liczba: ")
print(najwieksza_liczba)

end_number = 100

for numbers in range(0,end_number + 1,2):
    print(numbers, end=" ")