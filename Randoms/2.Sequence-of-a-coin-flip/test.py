input_arr = ["HHHTTHHH", 3, 2]


def kesh_solution(arr):
    modified_seq = arr[0].replace("HT", "H T").replace("TH", "T H")
    streak_count = sum(1 for streak in modified_seq.split(" ") if len(streak) == arr[1])
    return streak_count == arr[2]

