# NAJA-CLI

Naja is a command line tool that helps you set up a workspace for your vyper projects and
compile and generate ready to use json files for your contracts.
It will soon support automatic contract deployment python script creation 
and vyper contract testing.

## INSTALLATION

You can install the latest release using pip: 

pip install naja-cli==0.6

## USAGE

naja init					=> will set up a workspace in the current location<br/>
naja init --path			=> will set up a workspace in the specified path<br/>

naja compile				=> compile all the contracts in the Contracts folder<br/>
naja compile --contract		=> compile the specified contract in the Contract folder<br/>
