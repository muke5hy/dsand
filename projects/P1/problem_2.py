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

    cfiles_dir = []
    path = os.getcwd() + "/" + path
  
    extension = re.findall(r'(\w+\.\w+$)', path)
    #print(extension)
    if len(extension) > 0:
        print("Invalid path: {}".format(extension))
        return None
              
    # If path does not exist, return False    
    if not os.path.exists(path):
        print("Path: {} does not exist!".format(path))
        return None 

    for root, dirs, files in os.walk(path):
        for file_name in files:
            if fnmatch.fnmatch(file_name, suffix):
                if root not in cfiles_dir:
                    cfiles_dir.append(root)

    if len(cfiles_dir) == 0:
        print("File(s): {} not found!".format(suffix))
        return None
    else:   
        return cfiles_dir
    
if __name__ == "__main__":
    path = "testdir"
    print(f"Path {path} === ", find_files("*.c", path), end='\n\n')

    path = "testdir/subdir3"
    print(f"Path {path} === ", find_files("*.c", path), end='\n\n')

    path = "testdir/subdir4"
    print(f"Path {path} === ", find_files("*.c", path), end='\n\n')

    path = "testdir/test.h"
    print(f"Path {path} === ", find_files("*.c", path), end='\n\n')