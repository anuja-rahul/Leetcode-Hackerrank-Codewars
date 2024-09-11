import math


def count_divisors(n):
    divisors = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == n // i:
                divisors += 1
            else:
                divisors += 2
    return divisors


def get_triangle_num(num1, num2):
    for i in range(num1, num2):
        triangle_num = int((i * (i + 1)) / 2)
        divisor_count = count_divisors(triangle_num)
        # print(f"triangle num: {triangle_num}, divisor count: {divisor_count}")
        if divisor_count >= 500:
            print(f"triangle_num: {triangle_num}, divisor_count: {divisor_count}")
            break


get_triangle_num(1000, 400000)
