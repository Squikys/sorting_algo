import os
import pathlib
txt_is_found = False
pdf_is_found = False
psd_is_found = False
ai_is_found = False
def file (fileType,folderName):
    if fileType in file_list[files]:
        if not(pdf_is_found) :
            os.mkdir(folderName)
            pdf_is_found = True
        newpath = folderName+'/'+file_list[files]
        pathlib.Path(file_list[files]).rename(newpath)

dir = os.getcwd()
print(dir)
file_list = os.listdir(dir)
for files in range(0,list.__len__(file_list)):
    file(".pdf","pdf")
    if ".psd" in file_list[files]:
        if not(psd_is_found) :
            os.mkdir("psd")
            psd_is_found = True
        newpath = 'psd/'+file_list[files]
        pathlib.Path(file_list[files]).rename(newpath)
    if ".ai" in file_list[files]:
        if not(ai_is_found) :
            os.mkdir("ai")
            ai_is_found = True
        newpath = 'ai/'+file_list[files]
        pathlib.Path(file_list[files]).rename(newpath)
    if ".txt" in file_list[files]:
        if not(txt_is_found) :
            os.mkdir("txt")
            txt_is_found = True
        newpath = 'txt/'+file_list[files]
        pathlib.Path(file_list[files]).rename(newpath)
