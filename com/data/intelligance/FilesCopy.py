import os
import shutil

"""
PURPOSE:
Filtering the files based on extension
split it and copied into approriate folders
"""
os.chdir(r'C:\Users\bhanu\Desktop\input')
os.mkdir('csvfilefolder')
os.mkdir('jsonfilefolder')
for v in os.listdir():
    name,ext=os.path.splitext(v)
    print(name)
    print(ext)
    if ext=='.json':
        shutil.move(v,'jsonfilefolder')
    if ext=='.csv':
        shutil.move(v,'csvfilefolder')
shutil.copytree(r'C:\Users\bhanu\Desktop\input',r'C:\Users\bhanu\Desktop\output')
