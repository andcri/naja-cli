from setuptools import setup, find_packages

setup(
    name="naja_cli",
	version="0.2",
	description="test of naja to testpypi",
	packages=find_packages(),
	entry_points = {
		'console_scripts' : ['naja=naja.naja:main']
	}

)
