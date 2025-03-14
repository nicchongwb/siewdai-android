import os

def setup_proj_dirs(dirs):
    for dir in dirs:
        if not os.path.isdir(dir):
            os.makedirs(dir)
