from __future__ import print_function
import os
import os.path
import platform as pl
from getpass import getuser as user_name
from config_manager import Config








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
	conf = Config()
	if not conf.is_set("downloads_path", "documents_path"):
		downloads_path, documents_path = get_downloads_and_documents_path()
		conf.add(("downloads_path",downloads_path),("documents_path",documents_path))
	else:
		downloads_path, documents_path = conf.get("downloads_path", "documents_path")

	print(downloads_path, documents_path)
	'''
	if check_download_path(downloads_path):
		root, dirs, files = os.walk('.').next()
		print(root, dirs, files)
			

	else:
		raise Exception("Download directory not found")
	'''




any

if __name__ == '__main__':
	main()


'''

os.path.split(path)

    Split the pathname path into a pair, (head, tail) where tail is the last pathname component and head is everything leading up to that. The tail part will never contain a slash; if path ends in a slash, tail will be empty. If there is no slash in path, head will be empty. If path is empty, both head and tail are empty. Trailing slashes are stripped from head unless it is the root (one or more slashes only). In all cases, join(head, tail) returns a path to the same location as path (but the strings may differ). Also see the functions dirname() and basename().

'''