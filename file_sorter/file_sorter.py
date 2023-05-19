import os
import shutil


def sort_files(folder_path):

    # If folder_path does not exist, return empty
    if not os.path.exists(folder_path):
        print("Folder path does not exist.")
        return {}

    # Convert the folder path to the appropriate format based on the operating system
    folder_path = os.path.abspath(folder_path)
    # Create a list of all files in the folder
    files = os.listdir(folder_path)

    # Create a dictionary to store the file extensions and their corresponding subfolder paths
    extensions = {}

    # Iterate over each file in the folder
    for file in files:
        # Get the file extension
        _, file_extension = os.path.splitext(file)

        # Skip directories
        if not file_extension:
            continue

        # Create the subfolder path based on the file extension
        subfolder_path = os.path.join(folder_path, file_extension[1:])

        # Create the subfolder if it doesn't already exist
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)

        # Move the file to the subfolder
        file_path = os.path.join(folder_path, file)
        destination_path = os.path.join(subfolder_path, file)
        shutil.move(file_path, destination_path)

        # Update the extensions dictionary
        extensions[file_extension] = subfolder_path

    return extensions
