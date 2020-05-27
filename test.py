#!/usr/bin/python
import glob
import sys
import os
import shutil

fo = open('abc.txt','r')
print fo.read()
fo.close()
print("-----------------------------------------------------------------")

def find_file(l_path):
        list_of_files = []
        list_of_files = glob.glob(l_path)
        return list_of_files
filedir = find_file('/home/netcrk/Script/')
print(filedir)

print("-----------------------------------------------------------------")
#os.removedirs('/home/netcrk/Script/deleted/')
fd = []
fd = glob.glob('/home/netcrk/Script/deleted/*')
files = filter(lambda x: not x.endswith(("zip","tgz","gz")),fd)
print(files)
print("------------------------------------------------------------------")
pathlist = ['/home/netcrk/Script/deleted/', \
            '/home/netcrk/Script/temp/']
print(pathlist)

