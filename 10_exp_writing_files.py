import os

# provide the name for the output folder
output_folder_name = "output"

# provide a list of the files and folders
file_folders = os.listdir()

if output_folder_name not in file_folders:
    print(f"Folder '{output_folder_name}' not yet in directory")
    print("Creating.....")
    os.mkdir(output_folder_name)
else:
    print(f"Directory {output_folder_name} already exists")
    print("Skipping...")

# create a new file
file_name = "my_story"

# with is the 'context manager' for Python
with open(f"{output_folder_name}/{file_name}.txt", "w") as file:
    file.write("This is our story\n")
    file.write("About a programmer\n")
    file.write("The End")

