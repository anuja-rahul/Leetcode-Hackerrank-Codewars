grid_str = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


grid1 = grid_str.split('\n')
grid2 = [x.split(" ") for x in grid1]
grid3 = [[int(y) for y in x] for x in grid2]
# print(grid3)

data_list = []

# TODO: fix this

idx = 0
for i in range(0, len(grid3)):
    if len(grid3[i]) % 2 == 1:
        idx_list = [idx - 1, idx]
    else:
        idx_list = [idx + 1, idx]
    print(idx_list)
    # print(grid3[i])
    temp_list = []

    for nums in grid3[i]:
        temp_idx = grid3[i].index(nums)
        if temp_idx in idx_list:
            temp_list.append(nums)

    idx = grid3[i].index(max(temp_list))

    print(idx, max(temp_list))
    data_list.append(max(temp_list))

print(data_list)
print(sum(data_list))


