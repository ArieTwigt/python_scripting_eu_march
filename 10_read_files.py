#%% use file.read() to parse the content of a file as a single str
with open("output/my_story.txt", "r") as file:
    file_contents_str = file.read()

#%%
file_contents

#%% optionally you can split the string with the split.() method for str objects
file_contents_str.split("\n")

# %% use file.readlines to parse each line of the file as a seperate value for a list
with open("output/my_story.txt", "r") as file:
    file_contents_list = file.readlines()


#%% 
file_contents_list

# %%

# %%
