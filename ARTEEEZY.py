import crypt

print"          _____ _______ ______ ______ ________     __"
print"    /\   |  __ \__   __|  ____|  ____|___  /\ \   / /"
print"   /  \  | |__) | | |  | |__  | |__     / /  \ \_/ / "
print"  / /\ \ |  _  /  | |  |  __| |  __|   / /    \   /  "
print" / ____ \| | \ \  | |  | |____| |____ / /__    | |   "
print"/_/    \_\_|  \_\ |_|  |______|______/_____|   |_|   "
                             

print "email: maksimumride@gmail.com"                         
print "git: github.com/EnhboldH"

print "Feel free to report bug"
print "\n Press ^C to stop"

ans = raw_input("Do you want to continue? Y/N: ")
if ans == "Y" or ans == "y":
	#
	# Password Recovering
	#

	shadow = '/etc/shadow'
	passRecovery = open(shadow, "r")
	root = str(passRecovery.readline()).strip('\n')


	foo = ([pos for pos, char in enumerate(root) if char == "$"])
	salt = root[foo[0]:foo[len(foo)-1]]

	foo1 = ([pos for pos, char in enumerate(root) if char == ":"])
	encrypted_key = root[foo1[0]+1:foo1[1]]

	print "Salt is", salt
	print "Hash is", encrypted_key
	#
	# Bruteforcing
	#
	
	rockyou = '/root/Desktop/rockyou.txt'

	#lolz = '/root/Desktop/lolz.txt'
	#You can use your own dictionary
	counter = 0
	with open(rockyou) as f:
		while True:
			line = f.readline()
			k = line.split('\n')[0]
				
			if line == "":
				print "Sorry password not found :("
				break
			string = str(k)
			key = crypt.crypt(string, salt)
			
			#print "tested: ", string
			
			if(encrypted_key == key):
				print "Password found: ", string
				break
			counter += 1
			if counter % 500 == 0:
				print counter, "words tested"
else:
	print "     Thanks for using     "
	raise SystemExit


