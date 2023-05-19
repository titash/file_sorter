import pytest
from file_sorter.file_sorter import sort_files


def test_sort_files_valid_folder():
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
    # Provide an empty folder path
    folder_path = ""
    extensions = sort_files(folder_path)
    assert not extensions  # Assert that the dictionary is empty

