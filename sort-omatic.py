import os
import platform as pl
from getpass import getuser as user_name

def get_os():
	name = pl.system() #era figo anche .uname
	if name != 'Windows' and name != 'Linux':
		raise Exception("Cannot detect os. Stopped")
	return name

def get_downloads_and_documents_path():
	os_name = get_os()
	dl_path, dc_path= '', ''
	
	if os_name == 'Linux':
		dl_path = '/home/'+user_name()+'/Downloads'
		dc_path = '/home/'+user_name()+'/Documents'
		return dl_path, dc_path
	if os_name == 'Windows':
		disk = os.getcwd().split('\\')[0]
		dl_path = '\\'.join((disk, 'Users', user_name(), 'Downloads'))
		dc_path = '\\'.join((disk, 'Users', user_name(), 'Documents'))
		return dl_path, dc_path

def check_download_path(dl_path):
	try:
		os.chdir(dl_path)
		return True
	except:
		return False

def main():
	download_path, _ = get_downloads_and_documents_path()
	if check_download_path(download_path):
		print('directory found')
		print(os.getcwd())
	else:
		raise Exception("Download directory not found")
	

if __name__ == '__main__':
	main()
