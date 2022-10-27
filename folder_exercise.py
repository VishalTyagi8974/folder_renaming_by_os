import os
#this program take path as input, and then rename all files of that directory according to a function... 



x=input("input a path")
y=input("input a file")
z=input("input a format")

def folder_prettify(a,b,c):
    os.chdir(a)
    file_lis= os.listdir(a)
    f= open(b)
    unchn_file= f.readlines()
    f.close()
    i=0
    for file in file_lis:
        if file in file_lis:
            os.rename(file, file.capitalize())
        if os.path.splitext(file)[1]==c:
            os.rename(file,f"{i}.{c}")
            i=i+1
        if os.path.splitext(file)[0] in unchn_file:
            os.rename(file,file.lower())

folder_prettify(x,y,z)
