sum_squares = sum([i**2 for i in range(1, 101)])
square_sum = sum([i for i in range(1, 101)])**2

print(abs(sum_squares - square_sum))
