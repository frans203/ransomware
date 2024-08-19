import os
from cryptography.fernet import Fernet

files = []

currentDirectoryFiles = os.listdir("files")

#entering files directory and getting all the files from there
for file in currentDirectoryFiles:
    if file == 'malware.py' or file == 'thekey.key' or file == 'decrypt.py':
        continue
    #saving the directory from the files
    files.append("files/" + file)


#getting key
with open("thekey.key", 'rb') as key:
    secretkey = key.read()


#getting secret phrase
with open("secret_phrase.txt") as phrase:
    secretPhrase = phrase.read()

userPhrase = input('PLEASE ENTER THE SECRET CODE/PHRASE TO DECRYPT THE FILES\n')

if userPhrase != secretPhrase:
    while userPhrase != secretPhrase: 
        print('INVALID CODE/PHRASE!')
        userPhrase = input('PLEASE ENTER THE SECRET CODE/PHRASE TO DECRYPT THE FILES\n')


if userPhrase == secretPhrase:
    #for each file 
    for file in files:
        with open(file, 'rb') as openFile:
            #read its contents and save it
            contents_encrypted = openFile.read()
        # decrypt its contents with the key
        contents_decrypted = Fernet(secretkey).decrypt(contents_encrypted)
        #read the file again and save its content as the encrypted data
        with open(file, 'wb') as openFileToWrite:
            openFileToWrite.write(contents_decrypted)
    print("Files decrypted. Enjoy.")
    