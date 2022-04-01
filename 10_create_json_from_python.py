#%%
import json

config_dict = {}

config_dict['location'] = 'https://db.location.com'
config_dict['param_1']  = 'foo'
config_dict['param_2']  = 20
config_dict['param_3']  = [1,2,3, 'alpha', 'beta']


#%%
config_dict_str = json.dumps(config_dict)

#%%
with open("input/config.json", "w") as file:
    file.write(config_dict_str)

# %%
