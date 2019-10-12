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
import logging
from datetime import datetime

def compile_contracts(path='Contracts'):
	logging.basicConfig(level=logging.INFO, filename='Logs/contracts_compilation.log', filemode='a',\
						format=f'{datetime.now()}  - %(process)s - %(levelname)s - %(message)s')
	files = os.listdir(path)
	for contract in files:
		# check if the file is a .vy file
		if contract[-2:] == 'vy' or contract[-2:] == 'VY':
			try:
				test_compilation(contract)
				compile(contract)
				print(f"Contract {contract} compiled successfuly")
				logging.info(f"Contract {contract} compiled successfuly")
			except Exception as e:
				print("------")
				print(f"""Compile error for contract {contract}, you can check the full error at Logs/contracts_compilation_errors.log""")
				print("------")
				logging.error(f"{contract}"+"\n"+str(e))
		else:
			print(f'The file {contract} is not a vyper file, please check the file extention.')

def compile_contract(contract_name, path='Contracts'):
	logging.basicConfig(level=logging.INFO,filename='Logs/contracts_compilation.log', filemode='a',\
						format=f'{datetime.now()}  - %(process)s - %(levelname)s - %(message)s')
	files = os.listdir(path)
	if contract_name in files:
		try:
			test_compilation(contract_name)
			compile(contract_name)
			print(f"Contract {contract_name} compiled successfuly")
			logging.info(f"Contract {contract_name} compiled successfuly")
		except Exception as e:
			print("------")
			print(f"""Compile error for contract {contract_name}, you can check the full error at Logs/contracts_compilation_errors.log""")
			print("------")
			logging.error(contract_name+"\n"+str(e))

def compile(contract):
	path = f"Contracts/{contract}"	
	contract_json = open(f'Build/{contract[:-3]}.json', 'w') 
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

def test_compilation(contract):
	path = f"Contracts/{contract}"
	with open(path, 'r') as f:
		read_contract = f.read()
	vyper.compile_code(read_contract)
