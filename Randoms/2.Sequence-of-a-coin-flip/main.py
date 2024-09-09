from schemas import FlipDataInput
from typing import List
from python_datalogger import DataLogger

testlogger = DataLogger(name="TestLogger", propagate=True, level="DEBUG")


def sequence_result(values: FlipDataInput) -> bool:
    sequence = values.sequence
    length = values.length
    streak = values.streak

    c_l = 0
    c_s = 0
    p_c = sequence[0]

    for i in range(len(sequence)):
        c_c = sequence[i]
        p_c = sequence[i-1]

        # print(f"curr: {c_c}, prev: {p_c}")

        if sequence[i] == p_c or i == 0:
            c_l += 1
        else:
            c_l = 1

        if c_l == length:
            c_s += 1

        if c_l > length:
            c_s -= 1

        p_c = sequence[i]

    if c_s == streak:
        return True

    return False


@testlogger.logger
def solution(data: List[str | int]) -> bool:
    validated_data = FlipDataInput(sequence=data[0], length=data[1], streak=data[2])
    result = sequence_result(validated_data)
    print(result)
    return result


solution(["HHHTTHHH", 3, 2])
solution(["HHHHTTHHHTTTT", 4, 2])
solution(["HHHTTHHTTH", 2, 3])
