import math


def calc_circle(diameter: [int, float], multiplier= 1, round_value=1, return_radius=False) -> float:
    '''
    This is a function that calculates the surface of a circle.

    parameters:
    - diameter (float/int) e.g. 10
    - multiplier (int) - multiply the end result
    - round_value (int) - round the end result by the amount of decimals
    - return_radius (bool) - return the radius as well

    '''


    radius = diameter / 2 # create a local variable for the radius
    result = (math.pow(radius, 2) * math.pi) * multiplier
    result_rounded = round(result , round_value)

    if return_radius:
        return result_rounded, radius
    else: 
        return result_rounded


def give_name_of_script():
    print(f"2. The name of this script is {__name__}")
