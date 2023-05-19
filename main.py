from file_sorter.file_sorter import sort_files

folder_path = input(r"Enter the folder path: ")

extensions = sort_files(folder_path)

print(f"Files sorted by extension:")

for extension, subfolder_path in extensions.items():
    print(f"Extension: {extension}, Subfolder: {subfolder_path}")
