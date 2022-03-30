## Assignments

#%% Assignment 1
first_name = "Erling"
last_name  = "Haaland"

full_name = "{} {}".format(first_name, last_name)

#%% a. using '+' for concatenation
full_name_new = full_name + " Jr."
print(full_name_new)

#%% b. using the 'format' method
full_name_new = "{} Jr.".format(full_name)
print(full_name_new)

#%% c. using 'f' strings
full_name_new = f"{full_name} Jr."
print(full_name_new)


#%% Assignment 2.

#%% a. (not generic)
full_name_short = full_name_new.replace("rling", ".")
print(full_name_short)

#%% b. Only works if you have the seperate values
full_name_short = f"{first_name[0]}. {last_name} Jr."
print(full_name_short)

#%% c. Will work the most of the times, even when you do not have the seperate variables
full_name_list = full_name_new.split(" ")
first_letter   = full_name_list[0][0]
full_name_list[0] = first_letter + "."

full_name_short = " ".join(full_name_list)
print(full_name_short)


# %% Assignment 3
flower_list_1 = ['rose', 'tulip', 'lily']
flower_list_2 = ['dandelion', 'gerbera']

combined_flower_list = flower_list_1 + flower_list_2



#%% a. If you are sure that 'tulip' is at position 1
combined_flower_list[1] = 'daisy'


#%% b.If you do not know the exact position
id_tulip = combined_flower_list.index('tulip')
combined_flower_list[id_tulip] = 'daisy'


#%% c. List comprehension --> If all the tulips should be replaced
['daisy' if flower == 'tulip' else flower for flower in combined_flower_list]

# %%
