#%% Assignment 1
from datetime import date

my_birthday = date(2022,4,10)
date_today = date.today()

difference     = my_birthday - date_today
day_difference = difference.days

print(day_difference)

# %% Assignment

#%%
from math import pow, pi

diameter = 10
radius   = diameter / 2

surface = pow(radius, 2) * pi
surface_rounded = round(surface, 1)
print(surface_rounded)

# %% Assignment 3

import os

files_folders = os.listdir()

# %% Assignment 4

#%% a. 
import os

os.mkdir("our_functions")

# %% b.
try:
    os.mkdir("our_functions")
except FileExistsError:
    print("Directory  already exists")

# %% 3.

files_folders = os.listdir()

dir_name = "our_functions"

if dir_name not in files_folders:
    os.mkdir(dir_name)

# %%
