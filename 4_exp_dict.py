#%% Declaritive programming
my_dict = {"name": "Arie", 
           "city": "Amsterdam",
           "hobbies": ['cycling', 'football', 'tennis']}


#%% Imperative programming
my_dict_2 = {}

my_dict_2['name'] = "Arie"
my_dict_2['city'] = "Amsterdam"
my_dict_2['hobbies'] = ['cycling', 'football', 'tennis']

# %%
names_list = ['Arie', 'John', 'Mary', 'Peter']
# %%
names_list[0]
# %%
my_dict.values()
# %%
my_dict['age']


# %%
names_list = ['Arie', 'John', 'Mary', 'Peter']
ages_list = [10, 20, 30, 40]


#%%
my_dict_3 = dict(zip(names_list, ages_list))

# %%
my_dict_3['Mary']

#%%
my_dict = {"name": "Arie", 
           "city": "Amsterdam",
           "hobbies": ['cycling', 'football', 'tennis']}

# %% return the 2nd hobby from 'my_dict'

my_dict['hobbies'][1]

# %%
