import os

# provide the name for the output folder
selected_folder_name = input("Select the folder in which you want to insert the file (stories):\n") or "stories"
output_folder_name = f"output/{selected_folder_name}"

# provide a list of the files and folders
file_folders = os.listdir()

if output_folder_name not in file_folders:
    print(f"Folder '{output_folder_name}' not yet in directory")
    print("Creating.....")
    os.makedirs(output_folder_name, exist_ok=True)
else:
    print(f"Directory {output_folder_name} already exists")
    print("Skipping...")

# create a new file
selected_file_name = input("Provide the name for your file (my_story):\n") or "my_story"
file_name = selected_file_name

file_content = input("Insert the content of your file:\n") or ""

# with is the 'context manager' for Python
with open(f"{output_folder_name}/{file_name}.txt", "w") as file:
    file.write(file_content)

print("Debug")