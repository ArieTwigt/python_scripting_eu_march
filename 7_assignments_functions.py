#%% Assignments

#%% Assignment 1

# %% a.
def calc_contents(length, width, height):
    contents = length * width * height
    return contents



#%% b. Description and type hinting
def calc_contents(length: [int, float], width: [int, float], height: [int, float]) -> float:
    '''
    This function returns the contents

    parameters:
    - length
    - width
    - height
    '''
    
    contents = length * width * height
    contents_float = float(contents)
    return contents_float


#%%
calc_contents(length, width, height)

#%% Assignment 2

#%% a. 

def capitalize_names(names_list):
    names_list_capitalized = [name.capitalize() for name in names_list]
    return names_list_capitalized

#%%
names_list = ['jim', 'john', 'marc', 'danny', 'peter']

capitalize_names(names_list)

# %% b. With validation 
import sys

def capitalize_names(names_list, auto_cast=True):

    for idx, name in enumerate(names_list):
        if type(name) != str:
            if type(name) in [int, float] and auto_cast:
                names_list[idx] = str(name)
            else:
                raise TypeError(f"Error for value '{name}'. All values of the list should be of type 'str'\n or set 'auto_cast' to True for ints and floats")
                sys.exit(1)

    names_list_capitalized = [name.capitalize() for name in names_list]
    return names_list_capitalized

#%%
names_list = ['jim', 'john', {'name': 'arie'}, 'danny', 'peter']

capitalize_names(names_list)


#%% Assignment 3




