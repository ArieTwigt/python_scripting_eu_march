## Assignments




#%% Assignment 1.
with open("output/my_second_story.txt", "w") as file:
    file.write("Once there was a Python programmer\n")
    file.write("He wanted to do Data Science\n")
    file.write("Then he switched to R \n")
    file.write("\n")
    file.write("The End")


# %% Assignment 2.

#%% a
with open("output/my_second_story.txt", "r") as file:
    story_content = file.readlines()

# split the lines afterwards
story_content_list = [sentence.replace("\n", "")for sentence in story_content]

#%% b. Better
with open("output/my_second_story.txt", "r") as file:
    story_content_list = file.read().splitlines()


# %% Assignment 3/4
import os

story_content_list_upper = [sentence.upper() for sentence in story_content_list]
story_content_upper = "\n".join(story_content_list_upper)

output_folder = "output"
files_folders = os.listdir()

if output_folder not in files_folders:
    os.mkdir(output_folder)

with open("output/my_second_story_upper.txt", "w") as file:
    file.write(story_content_upper)
# %%
