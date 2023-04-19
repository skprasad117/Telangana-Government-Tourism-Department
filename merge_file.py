import os
import pandas as pd

directory = 'Dataset'
 
def read_directory(directory_name):
    directory = directory_name
    folders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory,folder))]
    
    read_files(folder_name = folders)
    return "success"

def read_files(folder_name):
    folders = folder_name
    files = dict()
    for folder in folders:
        files[folder] = [file for file in os.listdir(os.path.join(directory,folder))]

    read_merge_save(folders_in_directory = folders, files_in_folders = files)

def read_merge_save(folders_in_directory,files_in_folders):
    folders = folders_in_directory
    files = files_in_folders
    print(type(files))
    for folder in folders:
        df_1 = pd.DataFrame()
        for count,file in enumerate(files[folder]):
            if count == 0:
                df_1 = pd.read_csv(os.path.join(directory,folder,file))
            else :
                df_2 = pd.read_csv(os.path.join(directory,folder,file))
                df_1 = pd.concat([df_1,df_2],axis=0)
        try:
            os.makedirs("merged_files")
        except FileExistsError:
            pass
        df_1.to_csv(os.path.join('merged_files',folder+'.csv'), index= False)
    return None

print(read_directory(directory))
        