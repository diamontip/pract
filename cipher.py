'''
ToDo:
1. cipher program


'''
import string
shift_amt = 13
alphabet = string.ascii_lowercase
tab =string.maketrans(alphabet,alphabet[shift_amt:] + alphabet[:shift_amt])
print "shanmuga raja".translate(tab)
