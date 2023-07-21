import os
import pathlib

file_list = os.listdir(os.getcwd())

for a in range(len(file_list)):
    if file_list[a] != 'sorting_algo.py' and '.' in file_list[a]:
        worker = file_list[a]
        i=len(worker.split('.'))
        try:
            os.mkdir(worker.split('.')[i-1])
        except:
            pass    
        newpath = worker.split('.')[i-1]+'/'+file_list[a]
        pathlib.Path(file_list[a]).rename(newpath)
        
