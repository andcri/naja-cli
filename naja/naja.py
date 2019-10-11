"""
this file will be the command line interface that the user will use manage
the project
"""
import argparse
import sys
from naja.create_workspace import check_and_create_folder, check_and_create_configuration_file

class Naja():
	
	folders_names = ('Build', 'Contracts', 'Ganache_scripts', 'Rinkeby_scripts', 'Ropsten_scripts') 
	description = "Helps you manage your Vyper smart contract project"
	usage = "naja <command> [<args>]"

	def __init__(self):
		parser=argparse.ArgumentParser(description=self.description, usage=self.usage)
		parser.add_argument('command', help='the command to run')

		args = parser.parse_args(sys.argv[1:2])
		if not hasattr(self, args.command):
			print("This command does not exists")
			parser.print_help()
			exit(1)
		getattr(self, args.command)()
	
	def init(self):
		parser = argparse.ArgumentParser(description="Initialize the workspace for the project")
		parser.add_argument('--path')
		args = parser.parse_args(sys.argv[2:])
		if not args.path:
			print("Initializing project on current folder")
			for folder_name in self.folders_names:
				check_and_create_folder(folder_name)
			print("Project initialized")

		else:
			print(f"Initializing project on path={args.path}")
			for folder_name in self.folders_names:
				check_and_create_folder(folder_name, args.path)
			print("Project initialized")
	
	def compile(self):
		parser = argparse.ArgumentParser(description="Compile the contracts inside the Contracts folder")
		parser.add_argument('--contract')
		args = parser.parse_args(sys.argv[2:])
		if not args.contract:
			print("compiling contracts in the Contracts folder")
		else:
			print(f"compiling contract {args.contract} in the Contracts folder")

def main():
	Naja()
