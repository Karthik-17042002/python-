#cryptography is used for importing fernet module for generating key to encrypt the pwd with random text
from cryptography.fernet import Fernet



def write_key():
    #here generate_key in bytes modes
    key = Fernet.generate_key()
    #file open with write bytes mode .So we can append the bytes to the  file
    with open("key.key",'wb') as key_file:
        key_file.write(key)
#Uncomment if you wnat to generate the key
#write_key()

def load_key():
    load_key = open("key.key",'rb')
    key=load_key.read()
    load_key.close()
    return key



pwd = input("What is your master password ?")
key = load_key() + pwd.encode()
#passing the key into Fernet module to encrypt
fer = Fernet(key) 
def view():
       with open ('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pas = data.split("|")
            decrypt_pwd = fer.decrypt(pas.encode()).decode()
            print("Username: "+ user + "Password " + decrypt_pwd )

def add():
    name = input("Enter your acc name: ")
    pwd = input ("Enter your pwd :")
    encrypt_pwd = fer.encrypt(pwd.encode()).decode()
    with open ('passwords.txt','a') as f:
        f.write(name + "|"  + encrypt_pwd + "\n" )


while(1):
    mode = input("Would you like to add a new password or view existing ones? (view, add) or press to q exit ").lower()
    if mode == "q":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print(" Invalid Mode ")