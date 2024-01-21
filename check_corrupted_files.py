import os
import datetime
from concurrent.futures import ThreadPoolExecutor

def elapsed_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        start_time.strftime("%H:%M:%S")
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print("===" * 15)
        print("Elapsed time: ", end_time - start_time)
        print("===" * 15)
        return result
    return wrapper

input_folder = input("Target Folder: ")

def check_file(fpath):
    try:
        with open(fpath, 'rb') as fobj:
            is_jfif = b'JFIF' in fobj.peek(10)
        if not is_jfif:
            os.remove(fpath)
            return fpath, False
    except Exception as e:
        return fpath, e
    return fpath, True

@elapsed_time
def check_corrupted_files(path):
    num_deleted        = 0
    num_checked_file   = 0
    num_checked_folder = 0
    tasks              = []
    with ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(path):
            num_checked_folder += len(dirs)

            for fname in files:
                if fname.lower().endswith('.jpg') or fname.lower().endswith('.jpeg'):
                    fpath = os.path.join(root, fname)
                    task = executor.submit(check_file, fpath)
                    tasks.append(task)
                num_checked_file += 1
                print(f"Checked file: '{os.path.abspath(fpath)}' ---- ID: {num_checked_file}") # If id disappering in terminal or passing file that's mean the file checked before.
        
        for task in tasks:
            fpath, result = task.result()
            if not result:
                num_deleted += 1
   
    print('\n/// SCAN LOG ///')
    print('---' * 15)
    print(f"Folder: {path}.")
    print('---' * 15)
    print(f"Checked {num_checked_folder} folders.")
    print('---' * 15)
    print(f"Checked {num_checked_file} files.")
    print('---' * 15)
    print(f"Deleted {num_deleted} corrupted images.")
    print('---' * 15, '\n')

check_corrupted_files(input_folder)
