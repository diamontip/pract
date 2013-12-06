'''
ToDo:
1. cipher by adjusting char positions - completed
2. cipher by dictionary
3. decrypt for both cipher 
4. option to convery text, file
5. save the new file
6. delete the original file

'''
import string

print "\nSelect your encrypt method: \n"
print "1. one"
print "2. two"
selection = raw_input (" > ").lower()
if selection in ['1', 'one']:
	shift_amt = 1
	alphabet = string.ascii_lowercase
	tab =string.maketrans(alphabet,alphabet[shift_amt:] + alphabet[:shift_amt])
	print "abcdefghijklmnopqrstuvwxyz".translate(tab)
elif selection in ['2','two']:
	print "pimbalikka pilabhi"	

else: 
	print "you didnt make a valid choice"
	
