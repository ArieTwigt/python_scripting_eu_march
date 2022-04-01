#%%
import json

with open("input/config.json", "r") as file:
    config_str = file.read()


#%%
config_dict = json.loads(config_str)

# %%
config_dict['location']
# %%
config_dict['param_3']
# %%
config_dict['param_1']
# %%
