#%%
from our_functions.calc_functions import calc_circle, give_name_of_script

#%%
if __name__ == "__main__":
    print(f"1. The name of this script {__name__}")
    give_name_of_script()
    print(calc_circle(10))
# %%
