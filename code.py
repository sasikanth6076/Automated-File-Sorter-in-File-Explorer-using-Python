#importing os(Operating systems) & shutil (shell utility) packages
import os, shutil

#assigning a variable (Folder_Path) to our current working folder
Temp_Folder_Path = r"C:\Users\sasikanthchowdhary.n\OneDrive - Mu Sigma Business Solutions Pvt. Ltd\Desktop\TEMP FOLDER"

#listdir() opening a folder and seeing what's inside.
File_View =  os.listdir(Temp_Folder_Path)
print(File_View)

#Creating new address links as a text (simply adding new folder title to the current file path to make a new path as a plain text) 
Organized_Files_Path = os.path.join(Temp_Folder_Path, 'Organized_Files')

#Checking if Organized_Files previously exists or not in TEMP FOLDER 
if not os.path.exists(Organized_Files_Path):
    os.mkdir(Organized_Files_Path)
    print("Organized_Files created successfully!")

#Organized files consists of  another 3 files internally, so creating a new address links as a text
Organized_Files_bmp_Path = os.path.join(Organized_Files_Path, 'bmp_Files')
Organized_Files_xlsx_Path = os.path.join(Organized_Files_Path, 'xlsx_Files')
Organized_Files_txt_Path = os.path.join(Organized_Files_Path, 'txt_Files')

#Checking if bmp_files  previously exists or not in Organized_Files
if not os.path.exists(Organized_Files_bmp_Path):
    os.mkdir(Organized_Files_bmp_Path)
    print("bmp_Files created successfully!")

#Checking if xlsx_files  previously exists or not in Organized_Files
if not os.path.exists(Organized_Files_xlsx_Path):
    os.mkdir(Organized_Files_xlsx_Path)
    print("xlsx_Files created successfully!")

#Checking if txt_files  previously exists or not in Organized_Files
if not os.path.exists(Organized_Files_txt_Path):
    os.mkdir(Organized_Files_txt_Path)
    print("txt_Files created successfully!")

for item in File_View:
    if item.endswith(".bmp"):
        source = os.path.join(Temp_Folder_Path,item)
        destination = os.path.join(Organized_Files_bmp_Path, item)
        shutil.move(source, destination)
        print(f'Moved : {item} into bmp_Files')

    elif item.endswith(".xlsx"):
        source = os.path.join(Temp_Folder_Path,item)
        destination = os.path.join(Organized_Files_xlsx_Path, item)
        shutil.move(source, destination)
        print(f'Moved : {item} into xlsx_Files')

    elif item.endswith(".txt"):
        source = os.path.join(files,item)
        destination = os.path.join(Organized_Files_txt_Path, item)
        shutil.move(source, destination)
        print(f'Moved : {item} into txt_Files')

    