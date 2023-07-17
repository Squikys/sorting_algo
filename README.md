# sorting_algo
edit the code if you want to sort more type of files

first declare global variable
and then add this:

        ""if fileType in file_list[files]:
                if not(global_variable) :
                    os.mkdir(folderName)
                    global_variable = True
                newpath = folderName+'/'+file_list[files]
                pathlib.Path(file_list[files]).rename(newpath)""
        
in the for loop

note: while declaring global variabe make it false

"fileType" must be in this format ".exe",".cpp" etc.

"folderName" is the name of folder in which youu want to store the file
