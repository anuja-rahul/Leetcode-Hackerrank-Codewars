def collatz_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length


def count_collatz_chain(number):
    longest_chain_num = None
    longest_chain = 0
    for i in range(1, number):
        curr_num = i
        curr_chain = collatz_length(curr_num)

        if curr_chain > longest_chain:
            longest_chain = curr_chain
            longest_chain_num = curr_num
    print(longest_chain_num, longest_chain)


count_collatz_chain(1000000)
