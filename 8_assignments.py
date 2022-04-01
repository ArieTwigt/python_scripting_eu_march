## Assignments

#%% Assignment 1
import datetime

get_day_of_week = lambda x: x.strftime("%A")
# %%
current_date = datetime.date.today()
get_day_of_week(current_date)


# %% Assignment 2
from collections import defaultdict

people_dict = defaultdict(lambda: 'Unknown')

#%%
people_dict['John'] = 20
people_dict['Jim'] = 30

#%%
people_dict['James']


# %% Assignment 3

def gen_day_names(current_date, max_days):

    num_days = 0
    
    while num_days < max_days:
        new_date = current_date + datetime.timedelta(days=num_days + 1)
        day_name = new_date.strftime("%A")
        num_days += 1
        yield day_name


#%%
current_date = datetime.date.today() # can be any date

day_gen = gen_day_names(current_date, 10)


#%%
next(day_gen)


# %%
print("Some code")
next(day_gen)
# %%
