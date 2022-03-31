#%%
family_dict = {}


#%%
person_1 = {"name": "John", 
            "age": 40,
            "hobbies": ['reading', 'cycling']}

person_2 = {"name": "Mary", 
            "age": 38, 
            "hobbies": ['tennis', 'painting'], 
            "pet": {"name": "Tommy", 
                    "type": "cat", 
                    "hobbies": ['scratching', 'eating']}}

#%%
family_dict['name'] = 'Jones'
family_dict['members'] = []

# %%
family_dict['members'].append(person_1)
family_dict['members'].append(person_2)

# %%
family_dict['members'][1]['pet']['hobbies'][1]
# %%
family_dict.items()
# %%
