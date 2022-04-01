#%%
from collections import defaultdict

#%%
person_dict = {}

person_dict['age']  = 40
person_dict['city'] = 'Amsterdam'

#%%
person_dict['age']
person_dict['city']
person_dict['job'] # <- returns an error


#%%
person_dict_2 = defaultdict(lambda: 'Unkown')

person_dict_2['age']  = 40
person_dict_2['city'] = 'Amsterdam'


#%%
person_dict_2['age']
person_dict_2['city']
person_dict_2['job'] # <- returns an error

# %%
