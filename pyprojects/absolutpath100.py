import os
import time 
fName = 'testdrill.txt'

fPath = 'C:\\pyprojects\\'

abPath = os.path.join(fPath,fName)
print(abPath)

dirs = os.listdir()
for file in dirs:
    if file.endswith('.txt'):
        print (file)
        
        mpath = os.path.join(fPath,file)
        
        mtime = time.ctime(os.path.getmtime(mpath))
        "time.ctime() converts to more easily readable time and date"
        print(mtime)
    
