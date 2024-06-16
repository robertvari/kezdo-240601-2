import os

def find_files(root_folder: str, file_list: list, ext: str=None, name: str=None):
    # check if folder path is valid
    assert os.path.isdir(root_folder), f"root_folder must be a valid path: {root_folder}"
    assert isinstance(file_list, list), "file_list must be of type list."

    # collect folder content os.listdir()
    folder_content = os.listdir(root_folder)

    # collect files and folders
    # create list from subfolders
    subfolders = []
    for i in folder_content:
        full_path = os.path.join(root_folder, i)
        if os.path.isfile(full_path):
            # add files to file_list
            file_list.append(full_path)
        else:
            subfolders.append(full_path)


    # recall find_files with new folder
    for folder in subfolders:
        find_files(folder, file_list, ext, name)



if __name__ == '__main__':
    files = []
    find_files(r"D:\Work\PythonSuli\kezdo-240601\alapok_2\test_folder", files)
    pass