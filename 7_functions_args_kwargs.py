#%% function with args --> tuple()
def greet(sentence, *args):
    names = args
    for name in names:
        print(f"{sentence} {name}, how are you doing?")

#%%
greet("Hello", "Arie", "Jim", "Mary", "Jane")

# %% kwargs --> dictionary
def describe(describe_sentence, **kwargs):
    objects = kwargs

    for key, value in objects.items():
        print(f"This is a {key}, with the name {value}")


#%%
describe("This is a", car="Volvo", pet="Bird")

# %%
def describe_full(sentece, *args, **kwargs):
    topics = args
    selected_objects = kwargs

    for idx, value in enumerate(topics):
        print(f"{value}")

    for key, value in selected_objects.items():
        print(f"{key}, {value}")

    pass


#%%
describe_full("This is", "The first", "The second", "The third", "The fourth", car="Volvo", pet="Bird")

# %%
