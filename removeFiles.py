import os
import shutil
import time
from datetime import date


path = input("Path of files - ")
if os.path.exists(path):
    print("True")
    print("")
    dat = os.walk(path)
    for i in dat:
        data = i
        print(data)

        destin = str(data[0])
        print(destin)
        newPath = os.path.join(path, destin)
        print(newPath)
        AllFiles = os.listdir(newPath)
        print(AllFiles)
        print("")

    for i in AllFiles:
        stat = os.stat(newPath+'/'+i)
        print("The stats of ", i)
        print(stat)
        print(stat.st_mtime)
        print("")
        now = time.time()
        newNow = now - 30*86400
        print(newNow)
        print("")
        if stat.st_mtime < newNow:
            print("true")
            os.remove(newPath+'/'+i)
            #shutil.rmtree(newPath+'/'+i)
        else:
            print("False")
else:
    print("The path does not exist")            
