"""
create the folders and subfolders for the project
"""

import os
import shutil

def check_and_create_folder(folder_name, path=''):
	
	if os.path.isdir(path+folder_name):
		print(f"dir {path+folder_name} exists, overrite with a new empty one?[Y/n]")
		while True:
			user_choice = input()
			if user_choice == 'Y' or user_choice == 'y' or user_choice == 'yes':
				print("removing folder and creating new one")
				# delete current folder 
				shutil.rmtree(path+folder_name)
				# create new folder 
				os.mkdir(path+folder_name)
				break
			elif user_choice == 'n':
				print("skipping")
				break
			else:
				print("Choice not valid, please choose between Y and n")
	else:
		os.mkdir(path+folder_name)
		print(f"Successfuly inizialized {folder_name} folder")
	

def check_and_create_configuration_file(file_name):
	pass

if __name__ == '__main__':
	for folder_name in folders_names:
		check_and_create_folder(folder_name)
	
	print("Project workspace inizialied")
