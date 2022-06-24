from encodings import utf_8
from tokenize import Name
from unicodedata import name
from cryptography.fernet import Fernet
from passwords import userpass
import sys
import os

key = Fernet.generate_key()
cryption = Fernet(key)
proceed = False
curly = ('}')

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
	try:
		assert prmpt == '1' or prmpt == '2'
		if prmpt == '1':
			new_pass()
	
	except:
		sys.exit()

def encrypt(a):
	# Encrypts password
	return cryption.encrypt(a)

def decrypt(a):
	# Decrypts password
	return str(cryption.decrypt(a), 'utf8')

'''
password = encrypt(b'password')

print (password)

print (decrypt(password))
'''

def new_pass():
	service = input('Enter service name: ')
	if service not in userpass:
		password = bytes(input('Enter password: '))
		f = open('password.py', 'ab+')
		f1 = open('password.py', 'a+')
		f.seek(-1, os.SEEK_END)
		f.truncate()
		f1.write(f'	\'{service}\' : {password}, \n{curly}')
		f.flush()
		f1.flush()
		f.close()
		f1.close()
		sys.exit()

if __name__ == '__main__':
	main()