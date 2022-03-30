## Assignments

#%% Assignment 1 - Assign a variable that holds the number of days until your next birthday

#%% a.
import datetime

my_birthday  = datetime.date(2022, 4, 29)
current_date = datetime.date.today()

difference = my_birthday - current_date
days_difference = difference.days

print(days_difference)

#%% Assignment 2 - Calculate the surface of a circle with a diameter of 10 (radius^ * pi)

#%%
import math

diameter = 10
radius = diameter / 2

surface_circle = math.pow(radius, 2) * math.pi
print(surface_circle)


#%% Assignment 3 - Create list that contains the files in your current working directory

#%% 
import os

files_folders = os.listdir()
print(files_folders)

# %% Assignment 4 - Add a directory with the name our_functions
import os # only has to be imported once per script


#%% a. Only works if the directory does not exist yet
os.mkdir("our_functions")

# %% b. Will also work if the directory already exists
try: 
    os.mkdir("our_functions")
except FileExistsError:
    print("Directory already exists")


#%% c. More elgant, only attempts when it is not present
current_files_folders = os.listdir()

dir_name = "our_functions"

if dir_name not in current_files_folders:
    os.mkdir("our_functions")
else:
    print("Directory already exists")
# %%
