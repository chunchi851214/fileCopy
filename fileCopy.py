# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 12:18:49 2022

@author: jim60
"""
#%%
import argparse
import shutil
import os
import time
#%%

# the description
msg = "Search and Copy the files from the root folder to the target folder."

# initialize parser with the description in help
parser = argparse.ArgumentParser(description = msg)

# add the options of parameters
parser.add_argument("-sd", "--store_dir", help = "Store directory path", type=str, default=".\\copy_files")
parser.add_argument("-kw", "--keywords", help = "Keywords of target files", type=str, nargs = '+', default=None)

#%%

# Search main function
def copy_files_with_keywords(args, folder_time):
    # Check the destination folder exists or not.
    # If not exists, create it.
    if not os.path.exists("{}\\{}".format(args.store_dir, folder_time)):
        os.makedirs("{}\\{}".format(args.store_dir, folder_time))
    # Search the target files in the folder and its subfolders
    for root, dirs, files in os.walk('.\\', topdown=True):
        # To skip the files in the store directory.
        if args.store_dir in root:
            continue
        else:
            for name in files:
                src_path = os.path.join(root, name)
                # Check the files are the target files or not
                for keyword in args.keywords:
                    if keyword in name:
                        dst_path = args.store_dir + "\\{}\\{}".format(folder_time, name)
                        # Check if the target files has existed in destination folder or not
                        if os.path.isfile(dst_path):
                            os.remove(dst_path)
                        shutil.copyfile(src_path, dst_path)
                        break


#%%

# Begin time
begin = time.time()
# Read arguments from CMD
args = parser.parse_args()
# folder time
folder_time = time.strftime("%y%m%d%H%M", time.localtime())
# Copy files
if args.keywords:
    print("Copy files with keywords...")
    copy_files_with_keywords(args, folder_time)
else:
    print("Nothing is entered.")
# End time
end = time.time()
# Execution time
duration = end - begin
print("Cost time: %.4fs" % duration)
