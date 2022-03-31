## Assignments

#%% Assignment 1.
vowels = 'aeouiy'
names_list = ['Jim', 'John', 'Marc', 'Danny', 'Peter']

new_names_list = []

for name in names_list:
    print(name)
    for letter in name:
        if letter.lower() in vowels:
            name = name.replace(letter, "") # replace the letter for an empty character
    
    new_names_list.append(name)

print(new_names_list)

# %% Assignment 2.
import datetime

current_date = datetime.date.today()

total_days = 10
days_range = range(1, total_days + 1)

for num_days in days_range:
    new_date = current_date + datetime.timedelta(days=num_days)
    day_name = new_date.strftime("%A")
    print(day_name)
    print(f"Over {num_days} day(s) it is {day_name}")

# %%
