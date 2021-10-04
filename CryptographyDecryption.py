#Decyption code for EEE3097S Project

import time #import time
import getpass
from cryptography.fernet import Fernet #import encryption package

#Get user input
outfile = getpass.getpass(prompt='Type The Name of the File to be Decrypted:')

with open('filekey.key', 'rb') as filekey:
    key = filekey.read() #open file with key

fernet = Fernet(key) #store fernet object in variable
  
with open(outfile, 'rb') as enc_file:
    encrypted = enc_file.read() #read encrypted file
  
start = time.time()  #start time
decrypted = fernet.decrypt(encrypted) #decrypt
end = time.time() #end time
  
with open('Decrpyted.csv', 'wb') as dec_file:
    dec_file.write(decrypted) #write decrypted data
    
print('It took '+str(end - start)+' seconds to decrypt the file') #print to user  