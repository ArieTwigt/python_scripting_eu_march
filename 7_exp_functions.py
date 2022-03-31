#%% define a function, with no parameter(s)
def greet_all():
    print("Hello everyone")


#%%
x = greet_all()

# %% a function without a parameter, with a 'return' statement
def ping():
    return "pong"

#%%
x = ping()    

# %%
def upper_name(name):
    name_upper = name.upper()
    return name_upper

#%%
upper_name("Arie")


#%% define a function to calculate a circle
import math


def calc_circle(diameter):
    radius = diameter / 2
    result = math.pow(radius, 2) * math.pi
    return result


# %%
calc_circle(10)

# %% Add a doc string with a explanation of the function
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


# %%
circle_diameter, circle_radius = calc_circle(diameter=10, round_value=3, return_radius=True)

# %%
circle_diameter

# %%
circle_radius

# %%
