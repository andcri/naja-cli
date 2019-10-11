"""
here we will have two functions, one that compiles all the contract in the default 
Contracts folder and another one that will compile only the user specified contract
that is inside the Contracts folder.
The compiled contracts will then be saved in the folder Build and will override previous
versios if they exists
"""

import os, json
import shutil
import vyper

def compile_contracts(path='Contracts'):
	files = os.listdir(path)
	for contract in files:
		# check if the file is a .vy file
		if contract[-2:] == 'vy' or contract[-2:] == 'VY':
			# try to compile the file, if we cannot we will notify that to
			# the user and compile the next file
			try:
				compile(contract)
				print(f"Contract {contract} compiled successfuly")
			except:
				print(f"Compile error for contract {contract}")
				# TODO add full error in a log file that i put inside the log folder

def compile_contract(contract_name, path='Contracts'):
	"""
	Here the user will be able to select only the contract that he wants to compile
	by name
	"""
	files = os.listdir(path)
	if contract_name in files:
		try:
			compile(contract_name)
			print(f"Contract {contract_name} compiled successfuly")
		except:
			print(f"Compile error on contract {contract_name}")
			# TODO add error stacktrace to log file

def compile(contract):
	path = f"Contracts/{contract}"	
	contract_json = open(f'Build/{contract}.json', 'w') 
	current_dir = os.curdir

	with open(path, 'r') as f:
		read_contract = f.read()
	
	smart_contract = {}
	smart_contract[current_dir] = read_contract
	compiled_contract_code = vyper.compile_codes(smart_contract, ['abi', 'bytecode'], 'dict')

	smart_contract_json = {
	'contract_name' :  contract,
	'abi' : compiled_contract_code[current_dir]['abi'],
	'bytecode' : compiled_contract_code[current_dir]['bytecode']
	}

	json.dump(smart_contract_json, contract_json)	
	contract_json.close()








	
