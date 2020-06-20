import math
import numpy
from functools import reduce

# Problem 1
# ans = 0
# for i in range (1, 1000):
#     if i % 3 == 0 or i % 5 == 0:
#         ans += i

# Problem 2
# def fib(a):
#     if a == 0:
#         return 1
#     elif a == 1:
#         return 2
#     else:
#         return fib(a-1) + fib(a-2)
# ans = 0
# a, b = 1, 2
# while b < 4000000:
#     if b % 2 == 0:
#         ans += b
#     b = a + b
#     a = b - a

# Problem 3
# def prime_factors(x):
#     factor = 2
#     factors = []
#     while (x > 1):
#         if x % factor == 0:
#             while x % factor == 0:
#                 x /= factor
#             factors.append(factor)
#         factor += 1
#     return factors
# prime_factors(600851475143)

# Problem 4
# (1000 - x) * (1000 - y)
# (1000000 - (1000 * (x + y)) + xy)
# 1000 * (1000 - (x + y)) + xy
# xy = 1000 - (x + y) since palindrome
# 1000 - x - y - xy = 0
# z = x + y
# 1000 - z - x(z - x)
# x(z - x) = xz - x^2
# 1000 - z = xz - x^2
# 1000 = xz - x^2 + z = x^2 - xz - z = -1000

# for z in range (2, 1000):
#     left = 1000 - z
#     right = int(str(left)[::-1])

#     if (z ** 2 - 4 * right) > 0:
#         r_1 = (z + math.sqrt(z ** 2 - (4 * right))) / 2
#         r_2 = (z - math.sqrt(z ** 2 - (4 * right))) / 2
#         if r_1.is_integer() or r_2.is_integer():
#             print (1000 * left + right)
#             print (1000 - r_1)
#             print (1000 - z + r_1)

# Problem 5
# primes = [16, 9, 5, 7, 11, 13, 17, 19]
# ans = reduce((lambda x, y: x * y), primes)
# print(ans)

# Problem 6
# for i in range (1, 20):
#     if ans % i != 0:
#         print(i)
#         print("bad")
# def sum_of_squares(n):
#     return n * (n + 1) * (2 * n + 1) / 6

# def square_of_sums(n):
#     return (n * (n + 1) / 2) ** 2

# print (square_of_sums(100) - sum_of_squares(100))

# Problem 7
def prime_sieve(n):
    return filter(lambda num: (num % \
        numpy.arange(2, 1+int(math.sqrt(num)))).all(), range(2, n+1))


# primes = list(prime_sieve(120000))
# print(len(primes))

# print(primes[10000])


# Problem 8
# digits = """7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"""
# cons = 13
# ans = 0
# cur, count = 1, 0
# for i in range(0, 1000):
#     digit = int(digits[i])
#     if digit == 0:
#         cur, count = 1, 0
#     else:
#         cur *= digit
#         count += 1

#     if count == cons:
#         ans = max(cur, ans)
#         cur /= int(digits[i - cons + 1])
#         count -= 1

# print(ans)

# Problem 9
# a ** 2 + b ** 2 = c ** 2
# a + b + c = 1000
# euclid's formula (from quadratic derivations)
# a = m ** 2 - n ** 2, b = 2mn, c = m ** 2 + n ** 2
# m ** 2 - n ** 2 + 2mn + m ** 2 + n ** 2 = 1000
# 2m ** 2 + 2mn = 1000
# m ** 2 + mn - 500 = 0
# m > n > 0
# m = (-n +- sqrt(n ** 2 - 2000)) / 2)

# for n in range(0, 1000):
#     r_1 = (-n + math.sqrt(n ** 2 + 2000)) / 2
#     if r_1.is_integer() and r_1 > 0:
#         m = r_1
#         a = m ** 2 - n ** 2
#         b = 2 * m * n
#         c = m ** 2 + n ** 2

#         print(a * b * c)
#         break

# Problem 10
print(sum(prime_sieve(2000000)))
