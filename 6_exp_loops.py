#%%
flower_list = ['lily', 'rose', 'gerbera', 'tulip']


#%%
for i in flower_list:
    print(i)

# %% more descriptive variables for the iterators
for flower in flower_list:
    print(flower)

# %% enumerate
for idx, value in enumerate(flower_list):
    print(f"The {value} is on the {idx + 1} position")

# %%
def my_fun():
    return 'Arie', 4, ['a', 'b']

#%%
x, y , z = my_fun()

# %% regular loop to change the values of a list
flower_list       = ['lily', 'rose', 'gerbera', 'tulip']
flower_list_upper = []

for flower in flower_list:
    flower_upper = flower.upper()
    flower_list_upper.append(flower_upper)


#%% a list comprehension to change the values of a list

[flower.upper() for flower in flower_list]
    
# %%
flower_list          = ['lily', 'rose', 'gerbera', 'tulip']
flower_list_filtered = []

for flower in flower_list:
    if flower != 'rose':
        flower_list_filtered.append(flower)
    else:
        print(f"'{flower}' is not allowed")

# %% applying an conditional statement to a list comprehension
[flower for flower in flower_list if flower != 'rose']


#%% 'else' clause applied ! the conditional statments switches to the left
[flower  if flower != 'rose' else None for flower in flower_list]


# %%
numbers_list = [4,8,1,11,23,90,4]

numbers_list_filtered = [number for number in numbers_list if number > 10]

print(numbers_list_filtered)

# %%
flower_list          = ['lily', 'rose', 'gerbera', 'tulip']

#%% the 'break' keyword stops with the entire loop --> no more iterations --> proceed with the rest of the script
for flower in flower_list:
    print(flower)
    if flower == 'gerbera':
        print("We have found it!")
        break

print("Proceed with the rest of the code")

# %% 'continue' will stop the current iteration
for flower in flower_list:
    print(flower)
    if flower == 'gerbera':
        #print("We will not describe this flower\nup to the next flower")
        continue
    print(f"This is a nice {flower}")

print("Proceed with the rest of the code")

# %% pass --> Is only a placeholder
class MyObject:
    pass

#%%
for flower in flower_list:
    print(flower)
    if flower == 'gerbera':
        pass
    print(f"This is a nice {flower}")

print("Proceed with the rest of the code")

# %%
numbers_list_2 = [4,8,1,11,23,90,4, 50, 23, 75, 11, 86]

low_numbers   = []
high_numbers = []

for number in numbers_list_2:
    if number >= 50:
        high_numbers.append(number)
    elif number < 50:
        low_numbers.append(number)
    else:
        print("Impossible")

# %%
[number for number in numbers_list_2 if number >= 50]

#%%
[number for number in numbers_list_2 if number < 50]



# %%
score = 0


while score < 100: # infinite as long the condition is true, untill the condition becomes Flase
    print(f"Score is {score}\n\nAdd to the score")
    score += 10

# %%
names_list = ['Arie', 'James', 'Jim', 'Mary', 'John']

table_guests = []
max_guests = 4

while len(table_guests) < max_guests:
    next_guest = names_list.pop(0)
    table_guests.append(next_guest)
    print(f"The next guest '{next_guest}' is added to the table")
    print(f"The table now has {len(table_guests)} guests.")

# %%
names_list = ['Arie', 'John', 'Mary', 'Peter']
ages_list = [10, 20, 30, 40]

persons_dict = dict(zip(names_list, ages_list))
# %%
for key, value in persons_dict.items():
    print(f"{key} if {value} years old")

# %%
for age in persons_dict.values():
    print(age)
# %%
for key in persons_dict.keys():
    print(key)
# %%
person_1 = {"name": "John", 
            "age": 40,
            "hobbies": ['reading', 'cycling']}

person_2 = {"name": "Mary", 
            "age": 38, 
            "hobbies": ['tennis', 'painting'], 
            "pet": {"name": "Tommy", 
                    "type": "cat", 
                    "hobbies": ['scratching', 'eating']}}


family_dict = {}
family_dict['name'] = 'Jones'
family_dict['members'] = [person_1, person_2]

#%% display all the hobbies
for idx, person in enumerate(family_dict['members']):
    print(f"Person {person['name']} has the following hobbies")
    for idx, hobby in enumerate(person['hobbies']):
        print(f"{idx + 1}: {hobby}")
    print("\n")


#%%