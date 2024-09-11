num = str(2 ** 1000)
num_list = [x for x in num]
num_list = [int(x) for x in num_list]
sum_of_num = 0

for n in num_list:
    sum_of_num += n
print(sum_of_num)
