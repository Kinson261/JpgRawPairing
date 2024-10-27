"""
This script is used to delete files not having a JPG/RAW pair in a directory

author: @kinson
date: september 2024
"""

import os
import dotenv

from utilities import *


if __name__ == '__main__':
    dotenv.load_dotenv()

    EXT_JPG = os.getenv('JPG_EXT')
    EXT_RAW = os.getenv('RAW_EXT')
    print(EXT_JPG)
    print(EXT_RAW)
    EXCLUDE_FOLDERS = [os.getenv('EXCLUDE_FOLDERS')]

    args = argparser()
    dry_run = args.dry_run
    verbose = args.verbose
    path = args.path
    path = pathParser(path)

    print(f"Scanning folder...\n{path}")
    print(f"dry run = {dry_run}")
    print(f"verbose = {verbose}")

    jpg, raw = listFiles(path, EXT_JPG, EXT_RAW, EXCLUDE_FOLDERS)
    no_pair = compareLists(jpg, raw, EXT_JPG, EXT_RAW)
    deleteFilesFromList(no_pair, path, dry_run)
