import os
import platform as pl
from getpass import getuser as user_name

def get_os():
	name = pl.system() #era figo anche .uname
	if name != 'Windows' and name != 'Linux':
		raise Exception("Cannot detect os. Stopped")
	return name

def get_download_path():
	os_name = get_os()
	if os_name == 'Linux':
		return '/home/'+user_name()+'/Downloads'
	if os_name == 'Windows':
		dlpath = '\\'
		disk = os.getcwd().split('\\')[0]
		return dlpath.join((disk), 'Users', user_name(), Downloads)
def main():
	print get_download_path()

if __name__ == '__main__':
	main()
