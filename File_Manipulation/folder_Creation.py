import os

dir = os.getcwd()
name_list = ["API_Calls", "Training","Security","Games","Email","Scraping","OOP","Everyday_Use","Testing", "Python_Art","CLI","File_Manipulation"]
for x in name_list:
     # os.mkdir(os.path.join(dir,name_list)) that was the way without validation, just a quick one liner
     folder_path = os.path.join(dir,x)
     if not os.path.exists(folder_path):
         os.mkdir(folder_path)
         print(f"{x} folder created")
     else:
        print(f"{x} already exists")