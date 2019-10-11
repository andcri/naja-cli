"""
create the folders and subfolders for the project
"""

import os
import shutil

folders_names = ('Build', 'Contracts', 'Ganache_scripts', 'Rinkeby_scripts', 'Ropsten_scripts')

def check_and_create_folder(folder_name):
	
	if os.path.isdir(folder_name):
		print(f"dir {folder_name} exists, overrite with a new empty one?[Y/n]")
		while True:
			user_choice = input()
			if user_choice == 'Y' or user_choice == 'y' or user_choice == 'yes':
				print("removing folder and creating new one")
				# delete current folder 
				shutil.rmtree(folder_name)
				# create new folder 
				os.mkdir(folder_name)
				break
			elif user_choice == 'n':
				print("skipping")
				break
			else:
				print("Choice not valid, please choose between Y and n")
	else:
		os.mkdir(folder_name)

def check_and_create_configuration_file(file_name):
	pass

if __name__ == '__main__':
	for folder_name in folders_names:
		check_and_create_folder(folder_name)
	
	print("Project workspace inizialied")
