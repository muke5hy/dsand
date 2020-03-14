import os, fnmatch
import re

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """

    path_list = list()

    try:
        dir_path = os.listdir(path) 
    except:
        return [] 
    
    for item in dir_path:
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            path_list += find_files(suffix, full_path)
        elif os.path.isfile(full_path) and item.endswith(suffix):
            path_list.append(path + "/" + item)
    
    return path_list
    
if __name__ == "__main__":
    path = "testdir"
    print(f"Path {path} === ", find_files(".c", path), end='\n\n')

    path = "testdir/subdir3"
    print(f"Path {path} === ", find_files(".c", path), end='\n\n')

    path = "testdir/subdir4"
    print(f"Path {path} === ", find_files(".c", path), end='\n\n')

    path = "testdir/test.h"
    print(f"Path {path} === ", find_files(".h", path), end='\n\n')
    
    
    path = "testdir"
    print(f"Path {path} === ", find_files("", path), end='\n\n')
    
    path = ""
    print(f"Path {path} === ", find_files(".h", path), end='\n\n')