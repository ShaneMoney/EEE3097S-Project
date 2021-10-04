#Encryption code for EEE3097S Project

import time #import time
import getpass
from cryptography.fernet import Fernet #import encryption package

#Get user input
infile = getpass.getpass(prompt='Type The Name of the File to be Encrypted:')

key = Fernet.generate_key() #generate key
  
with open('filekey.key', 'wb') as filekey:
   filekey.write(key) #write key to file 
   
with open('filekey.key', 'rb') as filekey:
    key = filekey.read() #open file with key
    
fernet = Fernet(key) #store fernet object in variable

with open(infile, 'rb') as file:
    original = file.read() #open file to be encrypted
    
start = time.time() #start time
encrypted = fernet.encrypt(original) #encrypt file
end = time.time() #end time

with open('Encrypted '+ infile, 'wb') as encrypted_file:
    encrypted_file.write(encrypted) #write encrypted data to file
  
print('It took '+str(end - start)+' seconds to encrypt the file') #print to user  



