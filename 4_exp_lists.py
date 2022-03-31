#%%
numbers_list = [1,2,3,4,5]
# %%
numbers_list.append(3)
# %% is a method of a 'list' object --> Changes the state of the list
numbers_list.sort(reverse=True)

# %% sorted() is a global Python function --> Returns a new version of the iterable
sorted(numbers_list)

# %% 
sorted(list(set(numbers_list)), reverse=True)
# %% get slices of a list
numbers_list[5:8]


# %%
names_list = ['Arie', 'John', 'Mary', 'Peter']
#                0       1       2        3
#              -4        -3     -2       -1

#%%
names_list[3]
# %%
names_list[-3:-1]
# %%
names_list[-3]


#%%
my_list = [1,2,3,4,5]
my_list_2 = ['a', 'b', 'c']

#%%
my_list.append(my_list_2)

# %%
my_list[5][1]
# %%
