f_name = input("Enter name of the full file with extension : ")
f_ext = f_name[f_name.index(".")+1:len(f_name)+1]
print("The extension of the file is",end =" " + f_ext)
if ( f_ext == "py"):
    print("'Python'")
elif(f_ext == "docx"):
    print("'Word'")
elif(f_ext == "jpg"):
    print("'Photo file")
elif(f_ext == "txt"):
    print("'Text file or Notepad'")
else:
    print("'Other format'")