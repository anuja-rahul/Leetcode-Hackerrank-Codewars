from schemas import FlipDataInput
from typing import List
from python_datalogger import DataLogger

testlogger = DataLogger(name="TestLogger_02", propagate=True, level="DEBUG")


def sequence_result(values: FlipDataInput) -> bool:
    sequence = values.sequence
    length = values.length
    streak = values.streak

    c_l = 0
    p_l = 0
    c_s = 0

    for i in range(len(sequence)):
        p_c = sequence[i-1]
        if sequence[i] == p_c or i == 0:
            c_l += 1
        else:
            c_l = 1
        if c_l >= length:
            c_s += 1
        if c_l > length:
            c_s -= 1
            if p_l == length:
                c_s -= 1
        p_l = c_l

    if c_s == streak:
        return True
    return False


@testlogger.logger
def solution(data: List[str | int]) -> bool:
    validated_data = FlipDataInput(sequence=data[0], length=data[1], streak=data[2])
    result = sequence_result(validated_data)
    print(result)
    return result


# Check the log file for time duration of each run
solution(["HHHTTHHH", 3, 2])            # Pass
solution(["HHHHTTHHHTTTT", 4, 2])       # Pass
solution(["HHHTTHHTTHHHTT", 2, 4])      # Pass
solution(["HHHTHHH", 2, 3])             # Fail
solution(["HHHTTTTHHH", 3, 3])          # Fail
solution(["HHTTTHHHTHHHH", 2, 1])       # Pass
# solution(["HHHTTTTHHHHHHHHH", 9, 1])    # Fail - should return Validation error
