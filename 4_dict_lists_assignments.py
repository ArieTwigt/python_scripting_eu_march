## Assignments

#%% Assignment 1

#%% a.

person_1 = {"name": "James",
            "age": 30,
            "hobbies": ['cycling', 'reading', 'tennis']}

#%% b. 
person_1 = {}

person_1['name'] = "James"
person_1['age']  = 30
person_1['hobbies'] = ['cycling', 'reading', 'tennis']


#%% Assignment 2
person_1 = {"name": "John", 
            "age": 40,
            "hobbies": ['reading', 'cycling']}

person_2 = {"name": "Mary", 
            "age": 38, 
            "hobbies": ['tennis', 'painting'], 
            "pet": {"name": "Tommy", 
                    "type": "cat", 
                    "hobbies": ['scratching', 'eating']}}

person_3 = {"name": "Michael", 
            "age": 12,
            "hobbies": ['gaming', 'programming']}

person_4 = {"name": "Ann", 
            "age": 15,
            "hobbies": ['writing', 'boxing']}


#%% a. 
family_dict = {}
family_dict['name'] = 'Jones'
family_dict['members'] = [person_1, person_2, person_3, person_4]



#%% b. 

family_dict = {}
family_dict['name'] = 'Jones'
family_dict['members'] = []  # You first need to initiate the empty list before you can 'append' items to it


family_dict['members'].append(person_1)
family_dict['members'].append(person_2)
family_dict['members'].append(person_3)
family_dict['members'].append(person_4)

#%% c. 
family_dict = {}
family_dict['name'] = 'Jones'
family_dict['members'] = []

# the '.extend()' method can be used if you want to 'append' multiple items to a list
family_dict['members'].extend([person_1, person_2, person_3, person_4])

# %%
