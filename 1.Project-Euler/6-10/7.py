counter = 1
number = 2
last_prime = 2

while counter < 10001:
    number += 1
    for i in range(2, number//2 + 2):
        if number % i == 0:
            break
    else:
        counter += 1
        last_prime = number


print(last_prime)
