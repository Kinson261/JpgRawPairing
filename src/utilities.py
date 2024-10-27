import glob
import os
import sys
import time

import alive_progress
import argparse
import send2trash


def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str, required=True, help='path or list of paths to perform scanning')
    parser.add_argument('--dry-run', action='store_true', help='dry run', default=False)
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose', default=False)
    args = parser.parse_args()
    return args

def pathParser(path):
    if not os.path.exists(path):
        print(f"{path} does not exist")
        sys.exit(1)
    if not os.path.isdir(path):
        print(f"{path} is not a directory")
        sys.exit(1)

    if os.name == 'nt':
        path = path.replace('/', '\\')
    return path

def listFiles(path:str, ext_JPG:str, ext_RAW:str, exclude_folders:list):
    exclude_folders = exclude_folders[0].split(", ")
    """
    Using glob, list all files containing in the path directory except in the exclude folders recursively
    """
    JPG_files = [f for f in glob.iglob(os.path.join(path, '**', f'*.{ext_JPG}'), recursive=True) if not any(folder in f for folder in exclude_folders)]
    RAW_files = [f for f in glob.iglob(os.path.join(path, '**', f'*.{ext_RAW}'), recursive=True) if not any(folder in f for folder in exclude_folders)]

    files = glob.glob(os.path.join(path, '**', f'*'), recursive=True)
    
    with alive_progress.alive_bar(len(files)) as bar:
        for file in files:
            time.sleep(0.001)
            bar()
     
    print(f"Found {len(JPG_files)} JPG files and {len(RAW_files)} RAW files")

    return [JPG_files, RAW_files]

def compareLists(JPG_files:list, RAW_files:list, ext_JPG:str, ext_RAW:str)->list:
    NOPAIR_files = []

    for filename in JPG_files:
        if filename.replace(ext_JPG, ext_RAW) not in RAW_files:
            NOPAIR_files.append(filename)
    for filename in RAW_files:
        if filename.replace(ext_RAW, ext_JPG) not in JPG_files:
            NOPAIR_files.append(filename)
            
    return NOPAIR_files

def deleteFilesFromList(files:list, path:str, dry_run:bool):
    if (len(files) == 0):
        sys.exit(1)
  
    if not dry_run:
        _ = input("Are you sure to delete? [y/n]")
        i = 0 
        if ( _ == "y" or _ == "Y"):
            with alive_progress.alive_bar(len(files)) as bar:
                for filename in files:
                    send2trash.send2trash()
                    print(f"[{i+1}/{len(files)}] Deleting {os.path.join(path, filename)}")
                    i += 1
                    time.sleep(0.1)
                    bar()