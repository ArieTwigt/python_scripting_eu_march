#%%
name = "Arie"
age  = 40
city = "Amsterdam"

#%%
name_list = ['Arie', 'Jim']
name_list[10]

#%%
'''
Object (Str)

- methods
    - replace
    - capitalize
- attributes
    - len


'''


#%% Conventions

'''

- lowercase for variables
    - myCity (camel case)
    - my_city (python)

- descriptive variable names
    - a
    - b

    - name
    - city 

- No spaces
    - my city

- Do not use reserved names


'''

#%%
print("Hello world!")
# %%
print = "paper"


#%%
print("Hello world")
# %%
my_name = "Arie"
# %%
my_name.replace(old, new)


#%%
my_names = ['Arie', 'John']

# %% normal concatenation
"Hello" + " " + my_name

# %% using format
city = "Amsterdam"
"Hello {}, how are things going in {}?".format(my_name, city)

# %% f string
f"Hello {my_name}, how are things going in {city}?"

# %%
age = 30
"Hello" + age
# %%

#%%
"Hello {}".format(age)

# %% split method
name = "Arie Twigt"
name.split(" ")

# %%
name_tuple = ('Arie', 'John')
name_list  = ['Arie', 'John']


#%%
name_list[0] = 'Mary'
name_list.append('Eric')
print(name_list)
# %%
name_tuple[0] = 'Mary'
# %%
my_list  = [] # list()
my_tuple = () # tuple()
my_dict  = {} # dict()