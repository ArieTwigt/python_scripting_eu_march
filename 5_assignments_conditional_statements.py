## Assignments


#%% Assignment 1, 2

name = "Arie"

#%% a. 
if "A" in name:
    print("Your name contains an 'A'")
else: 
    print("Your name does not contain an 'A'")

# %% b. Take lower- and uppercase into consideration \
#       this will also work for e.g. 'arie'

if "a" in name.lower():
    print("Your name contains an 'A'")
else: 
    print("Your name does not contain an 'A'")

#%% Assignment 3

name = "James"

# both defining the vowels as a string or list will work
# these are both subscriptable
vowels = 'aeouiy'
vowels = ['a', 'e', 'o', 'u', 'i', 'y']



#%% a. 


if name[0].lower() in vowels:
    print(f"Your name {name} begins with a vowel")
    new_name = name.replace(name[0], "B")
    print(f"Your name is changed from {name} to {new_name}")
else:
    print(f"Your name {name} does not begin with a vowel")
    new_name = name.replace(name[0], "A")
    print(f"Your name is changed from {name} to {new_name}")



#%% b. more scalable
import random
import string

name = "aaran"

vowels = ['a', 'e', 'o', 'u', 'i', 'y']
letters_list = list(string.ascii_lowercase)

# list comprehension
non_vowels = [letter for letter in letters_list if letter not in vowels]

# conditional statement
if name[0].lower() in vowels:
    #
    print("Your name begins with a vowel")
    
    # get a random letter
    random_letter = random.choice(non_vowels)
    random_letter_upper = random_letter.upper()

    new_name = name.replace(name[0], random_letter_upper, 1) # make sure 'replace' only replaces one occurance of the letter
    print(f"Your name is changed from {name} to {new_name}")
else:
    print("Your name begins with a vowel")
    
    # get a random letter
    random_letter = random.choice(vowels)
    random_letter_upper = random_letter.upper()

    new_name = name.replace(name[0], random_letter_upper, 1) # make sure 'replace' only replaces one occurance of the letter
    print(f"Your name is changed from {name} to {new_name}")



# %% Extra: (later) --> you can create a function from this sequence
