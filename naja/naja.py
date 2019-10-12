"""
this file will be the command line interface that the user will use manage
the project
"""
import argparse
import sys
from naja.create_workspace import check_and_create_folder, check_and_create_configuration_file
from naja.compile_contracts import compile_contracts, compile_contract

class Naja():
	
	folders_names = ('Build', 'Contracts', 'Logs','Ganache_scripts', 'Rinkeby_scripts', 'Ropsten_scripts') 
	description = """Helps you manage your Vyper smart contract project
Commands:

init => Create workspace in current folder

init --path => Create workspace in specified PATH

compile => Compile all the contracts in the Contracts folder
	   and save the abi and bytecode in a json file in the 
	   Build folder

compile --contract => Compile the specified contract in the
	   	   Contracts folder and save the abo and bytecode in
		   the Build folder"""
	usage = "naja <command> [<args>]"

	def __init__(self):
		parser=argparse.ArgumentParser(description=self.description, usage=self.usage, \
										formatter_class=argparse.RawTextHelpFormatter)
		parser.add_argument('command', help='the command to run')

		args = parser.parse_args(sys.argv[1:2])
		if not hasattr(self, args.command):
			print("This command does not exists")
			parser.print_help()
			exit(1)
		getattr(self, args.command)()
	
	def init(self):
		parser = argparse.ArgumentParser(description="Initialize the workspace for the project")
		parser.add_argument('--path', help="specify the PATH where to create the workspace")
		args = parser.parse_args(sys.argv[2:])
		if not args.path:
			print("Initializing project on current folder")
			for folder_name in self.folders_names:
				check_and_create_folder(folder_name)
			print("Project initialized")

		else:
			print(f"Initializing project on path={args.path}")
			for folder_name in self.folders_names:
				check_and_create_folder(folder_name, args.path+'/')
			print("Project initialized")
	
	def compile(self):
		parser = argparse.ArgumentParser(description="Compile the contracts inside the Contracts folder")
		parser.add_argument('--contract', help="the contract that you want to compile in the Contracts folder")
		args = parser.parse_args(sys.argv[2:])
		if not args.contract:
			print("Compiling contracts in the Contracts folder")
			compile_contracts()
		else:
			print(f"Compiling contract {args.contract} in the Contracts folder")
			compile_contract(args.contract)

def main():
	Naja()
