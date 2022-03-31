#%%
numbers_list = [9,2,3,4,5]

selected_number = numbers_list[0]
print(selected_number)


#%%
if selected_number < 10:
    print("This is larger than 10")
    print("So this was true")
else:
    print("That was not the case")

print("This is the rest of the code")

# %%

from operator import xor



if xor(selected_number < 10, selected_number != 9):
    print(selected_number)
    print("Apply someting to the script")
    selected_number += 10
    print(selected_number)

elif selected_number == 9:
    print("That was close")
    selected_number += 1
    print(selected_number)

print("This is the rest of the code")

# %%
numbers_list 
# %%
if 6 in numbers_list:
    print("Present")
else:
    print("Not present")
# %%
