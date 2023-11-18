import os,shutil
source='D:/Downloads'
destination='D:/Whitehatjr/class 112/project/files'
listdir=os.listdir(source)
for files in listdir:
    name,extension=os.path.splitext(files)
    if extension=="":
        continue
    if extension in [ ".txt", ".doc", ".docx",".pdf"]:
        path1=source+'/'+files
        path2=destination+"/"
        path3=destination+"/"+files
        # print(path1)
        # print(path3)
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            shutil.move(path1,path3)