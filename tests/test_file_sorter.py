import shutil
import pytest
import os
from file_sorter.file_sorter import sort_files

@pytest.fixture
def setup_folder():
    # Set up the folder before the test case
    folder_path = "tests/data/unsorted_folder"
    os.makedirs(folder_path)  # Create the folder or perform other setup actions

     # Create 10 random files with different extensions
    extensions = ["txt", "csv", "xlsx", "json", "py", "jpg", "png", "pdf", "docx", "mp3"]
    for i in range(10):
        extension = extensions[i]
        file_name = f"file{i+1}.{extension}"
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "w") as f:
            f.write("This is a sample file.")
    yield folder_path  # Provide the folder path to the test case

    # Clean up the folder after the test case
    # Perform any cleanup actions here, such as deleting the folder
    shutil.rmtree(folder_path)

def test_sort_files_valid_folder(setup_folder):
    # Provide a valid folder path with files
    folder_path = "tests/data/unsorted_folder"  # Update with your folder path
    extensions = sort_files(folder_path)
    assert extensions  # Assert that the dictionary is not empty


def test_sort_files_nonexistent_folder():
    # Provide a folder path that does not exist
    folder_path = "nonexistent/folder/path"
    extensions = sort_files(folder_path)
    assert not extensions  # Assert that the dictionary is empty


def test_sort_files_empty_folder():
    # Provide the path to an existing empty folder
    folder_path = "tests/data/empty_folder"
    extensions = sort_files(folder_path)
    assert not extensions  # Assert that the dictionary is empty

