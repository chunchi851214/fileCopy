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
parser.add_argument("-sd", "--store_dir", help = "Store directory path", type=str, default="./copy_files")
parser.add_argument("-f", "--files", help = "Target files", type=str, nargs='+', required=True)

#%%

# Search main function
def copy_files(args):
    # Check the destination folder exists or not.
    # If not exists, create it.
    if not os.path.exists("{}".format(args.store_dir)):
        os.mkdir("{}".format(args.store_dir))
    # Search the target files in the folder and its subfolders
    for root, dirs, files in os.walk('./'):
        for name in files:
            src_path = os.path.join(root, name)
            if args.store_dir in src_path:
                continue
            # Check the files are the target files or not
            elif name in args.files:
                dst_path = args.store_dir + "/{}".format(name)
                # Check if the target files has existed in destination folder or not
                if os.path.isfile(dst_path):
                    os.remove(dst_path)
                shutil.copyfile(src_path, dst_path)


#%%

# Begin time
begin = time.time()
# Read arguments from CMD
args = parser.parse_args()
# Copy files
copy_files(args)
# End time
end = time.time()
# Execution time
duration = end - begin
print("Cost time: %.4fs" % duration)

    