import glob
import os
import shutil

# r - read
# a - append
# w - write
# x - create


# f = open("names.txt","r")
# print(f.read())

# print(f.readline())
# print(f.readline())

# for line in f:
#     print(line)
#
# f.close()


folderNames = ["Breaking_Bad", "Better_Call_Saul", "El_Camino", "Switzerland"]
source_path = "/Users/patrykloboda/PycharmProjects/pythonProject/"
desired_path = os.path.join(source_path, folderNames[0])
if not os.path.exists(desired_path):
    os.mkdir(source_path + folderNames[0])
    print(f"The folder {folderNames[0]} has been created in this address: {source_path}")
else:
    os.rmdir(desired_path)
    print(f"The folder: {folderNames[0]} was removed from this address: {source_path}")


# Show every pdf file in the downloads directory
download_dir = "/Users/patrykloboda/Downloads"

glob_downloads = os.path.join(download_dir, '*.pdf')


for filepath in glob.glob(glob_downloads):
    filename = os.path.basename(filepath) # Here im using os.path.basename() to extract name of files
    print(filename)

# shutil
#Test comment`

