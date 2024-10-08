import schemas
from typing import List
from python_datalogger import DataLogger

testlogger = DataLogger(name="TestLogger_01", propagate=True, level="DEBUG")


def to_kilograms(value: float, unit: str) -> float:
    to_kg = {
        'kg': 1,
        'g': 0.001,
        'µg': 1 / (10 ** 6),
        'mg': 1 / (10 ** 3),
        'lb': 0.453592
    }
    if unit in to_kg.keys():
        return value * to_kg[unit]


def to_meters(value: float, unit: str) -> float:
    to_m = {
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'ft': 0.3048,
        'µm': 1 / (10 ** 6)
    }
    if unit in to_m.keys():
        return value * to_m[unit]


def calculate_gravitational_force(values: schemas.MassDistanceBase,
                                  unit_values: schemas.MassDistanceUnitsBase) -> float:

    g = 6.67 * (10 ** -11)      # m**3 kg**-1 s**-2

    ob1_m = to_kilograms(values.mass_1, unit_values.unit_m1)
    ob2_m = to_kilograms(values.mass_2, unit_values.unit_m2)
    distance = to_meters(values.distance, unit_values.unit_d)

    """
    F = (G * m1 * m2) / d**2
    """

    gravitational_force = (g * ob1_m * ob2_m) / distance ** 2

    return gravitational_force


def format_to_scientific(value: float) -> str:
    if value == 0:
        return "0"

    exp = int(f"{value:.0e}".split('e')[1])
    coefficient = value / (10 ** exp)
    coefficient_string = f"{coefficient:.2f}"

    return f"{coefficient_string} * 10 ** {exp} N"


@testlogger.logger
def solution(arr_val: List[str], arr_unit: List[str]) -> float:
    mass_distance = schemas.MassDistanceBase(mass_1=arr_val[0], mass_2=arr_val[1], distance=arr_val[2])
    units = schemas.MassDistanceUnitsBase(unit_m1=arr_unit[0], unit_m2=arr_unit[1], unit_d=arr_unit[2])
    force = calculate_gravitational_force(mass_distance, units)
    formatted_force = format_to_scientific(force)
    print(formatted_force)
    return force


# check the log file for time duration of each run
solution(arr_val=[100, 16000, 90], arr_unit=["kg", "mg", "mm"])
solution(arr_val=[150, 100, 94500], arr_unit=["g", "g", "cm"])
solution(arr_val=[1700, 25700, 456230], arr_unit=["kg", "kg", "m"])
