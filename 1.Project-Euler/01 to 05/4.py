palindromes = []


for x in range(100, 1000):
    for y in range(100, 1000):
        result = x * y
        if str(result) == str(result)[::-1]:
            palindromes.append(result)

print(max(palindromes))