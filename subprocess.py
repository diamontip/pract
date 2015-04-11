'''
python script to collect system information using subprocess library. 
'''

#system information gather script. 

import subprocess

def shell_func():
	print "Setting the shell argument to a true value"
	subprocess.call('echo $HOME',shell=True)


def uname_func():
	uname = 'uname'
	uname_arg='-a'
	print "gathering system information with %s command:\n" %uname
	subprocess.call([uname,uname_arg])
	
def disk_func():
	diskspace = "df"
	diskspace_arg = "-h"
	print "gathering diskspace information %s command: \n" % diskspace
	subprocess.call([diskspace,diskspace_arg])

def in_out_func():
	output = subprocess.check_output(['ls','-1'])
	print 'have %d bytes in output' % len(output)
	print output
	
def main():
	shell_func()
	uname_func()
	disk_func()
	in_out_func()

main()
