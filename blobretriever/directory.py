import os
from pathvalidate import sanitize_filepath

def check(file_path):
    if os.path.exists(file_path):
        return True
    if file_path == sanitize_filepath(file_path, platform= 'auto'):
        return True
    return False