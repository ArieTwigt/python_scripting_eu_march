#%%
name_list = ['Arie', 'John', 'Jim']
name_list_2 = ['Peter', 'Mary', 'Ann']

#%%
for name in name_list:
    print(name)

# %%
def name_gen(name_list):
    num = 0
    while num < len(name_list):
        yield(f"Hello {name_list[num]}")
        num += 1

#%%
name_generator   = name_gen(name_list)
name_generator_2 = name_gen(name_list_2)

# %%
print("This is code")
print(next(name_generator))

#%%
print("Some other code")
print(next(name_generator_2))

print("Other code")
print(next(name_generator_2))
print(next(name_generator))
# %%
print(next(name_generator))
# %%
print(next(name_generator))
# %%
