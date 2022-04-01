import math

def calc_contents(length: [int, float], width: [int, float], height: [int, float]) -> float:
    contents = length * width * height
    contents_float = float(contents)
    return contents_float


def calc_pythagoras(a, b):
    c_sqrd = math.pow(a, 2) + math.pow(b, 2)
    c      = math.sqrt(c_sqrd)
    return c



