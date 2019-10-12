from setuptools import setup, find_packages

setup(
    name="naja_cli",
	version="0.6",
	description="command line tool for vyper smart contract development",
	licence="MIT",
	author="HippoB",
	packages=find_packages(),
	entry_points = {
		'console_scripts' : ['naja=naja.naja:main']
	}

)
