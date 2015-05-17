import os
print 'Example of a script vulnerable to injection'
print '() { :; };{ echo example; }'
print "/usr/bin/gpg|:() { :; };{ echo example; } -- Works with commands with options(ping -c, etc)"


x = raw_input("Enter : ")
gohomewhitepiggu = os.system("sha512sum {}".format(x)) # Any other command 
print(gohomewhitepiggu)
