#system information gather script. 

import subprocess

def uname_func():
	uname = 'uname'
	uname_arg='-a'
	print "collecting system information with %s command:\n" %uname
	subprocess.call([uname,uname_arg])
	
def disk_func():
	diskspace = "df"
	diskspace_arg = "-h"
	print "collecting diskspace information %s command: \n" % diskspace
	subprocess.call([diskspace,diskspace_arg])
	
def main():
	uname_func()
	disk_func()

main()
