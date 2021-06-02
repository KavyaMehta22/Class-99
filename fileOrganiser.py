import os
import shutil

path = input("Enter the name of the folder to be sorted:")
listOfFiles = os.listdir(path)

for file in listOfFiles :
    name, ext = os.path.splitext(file)
    ext = ext[1:]

 
    # This forces the next iteration,
    # if it is the directory
    if ext == '':
        continue

     # This will move the file to the directory
    # where the name 'ext' already exists    
    if os.path.exists(path+"/"+ext) :
        shutil.move(path+"/"+file, path+'/'+ext+'/'+file)

 # This will create a new directory,
    # if the directory does not already exist

    else:
        os.makedirs(path+"/"+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)