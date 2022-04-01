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

print("Hello")
sys.exit(1)
print("Still here")

names_capitalized = capitalize_names(names_list)

print(names_capitalized)