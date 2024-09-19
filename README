# What is this? 
This program targets hobbist and professionnal photographers. I always shoot JPG and RAW at the same time and I find myself having a hard time deleting pictures afterwards. I didn't find any program fitting my needs, so I decided to write one myself.  
  
This python script is used to delete unwanted files from your photoshoot. Instead of deleting your RAW, then your JPG, you can delete only one of them and the script will take care of the rest.  
It scans the indicated folder for files with specified extensions. After the scan, it compares all files and detect files, which don't have a pair and delete them.

# Installation  
Clone the repository using  

```
git clone https://github.com/Kinson261/JpgRawPairing.git
```
Jump into the directory and run:  

```
python -m pip install -r requirements.txt
```  
or 
```
python3 -m pip install -r requirements.txt
```  

# Get started  
Since each camera is different and I aim to make this mini-program as universal as possible. That is why I incorporated a .env file. 
## Populate your .env file 
    EXCLUDE_FOLDERS='Edited, edited'
    JPG_EXT='JPG'
    RAW_EXT='ARW'
WARNING: The python script goes through the indicated directory recursively. If you store your `Edited` pictures inside the scanned path, it will recognize these pictures too and since they may have been renamed and have no pair, it is important to exclude such folder.  
  
  Pay attention that this is **CASE-SENSITIVE**.  
  The variable `EXCLUDE_FOLDERS` can take a numerous arguments.  
  The variable `JPG_EXT` indicates the format of JPG files to be scanned, whereas `` is the format of RAWs.

## Run the script
```
python -m RAWChecker.py -p /my/folder/path
```
or 
```
python3 -m RAWChecker.py -p /my/folder/path
```
|**Flags**|**Description**|
|-----|--------|
|-p --path|path to be scanned|
|[--dry-run]|run the scan without deleting any files|
|[-v] [--verbose]|Show more output|

# ROADMAP
I plan to release a version of this program with a GUI and move awy from CLI for ease of use later this year.

# Report/Bug, Contributions
If you encounter any bug or unwanted behaviour, please report it in the tab `Issues`.  
  

You can contribute to this project too. I am open to any suggestions to make the app better. 