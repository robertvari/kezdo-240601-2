import os

def find_files(root_folder: str, file_list: list, ext: str=None, name: str=None):
    # check if folder path is valid
    assert os.path.isdir(root_folder), f"root_folder must be a valid path: {root_folder}"
    assert isinstance(file_list, list), "file_list must be of type list."

    # collect folder content os.listdir()
    

    # collect files and folders
    # add files to file_list
    # create list from subfolders

    # recall find_files with new folder



if __name__ == '__main__':
    files = []
    find_files(r"D:\Work\PythonSuli\kezdo-240601\alapok_2", files)