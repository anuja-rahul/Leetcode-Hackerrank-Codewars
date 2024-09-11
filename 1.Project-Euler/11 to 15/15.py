"""
C(m+n,m)
ex: for 2x2 grid with 2 directions (down and right)
(4!/(2!(4-2)!)) = 6
"""


def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


def get_lattice_paths(grid_length, directions):
    moves = grid_length * directions
    result = (factorial(moves)/(factorial(grid_length) * factorial((moves - grid_length))))
    return result


print(get_lattice_paths(20, 2))

