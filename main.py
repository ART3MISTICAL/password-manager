from cryptography.fernet import Fernet
import sys

key = Fernet.generate_key()

cryption = Fernet(key)

proceed = False

def main():
	# Main password to secure the script
	root = input('Enter root password: ')

	# Enter any password of your choice
	root_pass = '0'

	if root == root_pass:
		proceed = True
	
	else:
		sys.exit('Wrong password')

	if proceed == True:
		prompt()

def prompt():
	# Prompts the user for entering password or viewing them
	prmpt = input('Press (1) to enter password or (2) to view passwords: ')

def encrypt(a):
	# Encrypts password
	return cryption.encrypt(a)

def decrypt(a):
	# Decrypts password
	return cryption.decrypt(a)