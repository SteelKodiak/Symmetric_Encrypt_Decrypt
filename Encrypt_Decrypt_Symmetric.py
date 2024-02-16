"""
Warning: Do not use Fernet in a production environment or for legitimate personal use, until ready. 
Fernet library provides Symmetric encryption, meaning you have to have the key to decrypt the password. 

Fernet is US DoD compliant and provides AES-128 bit encryption, using PKCS7 padding. HMAC using SHA256 for authentication. 
"""
# Now we need to generate a key for the encryption/decryption project.
# You can modify the following code and use your own key; or use the random key generator. For practice and documentation, we are using the Fernet key gen. 

from cryptography.fernet import Fernet

def genkey():
# Generates a new key and places it in the current working directory
    key = Fernet.generate_key()             # Generates the key
    with open("dat.key", "wb") as key_file: # "w" should stand for write, and "b" stands for byte. 
        key_file.write(key)                 # Actually writes the key. 
    #print("Encryption key generated, keep this to decrypt: " "\n", key.decode(), "\n")        # Prints the key Generated. 

def loadkey():
#Loads symmetric encryption key for use
    return open("dat.key", "rb").read()     # "r" should stand for read, and "b" stands for byte.

Passwordinput = input("Password to Encrypt: ").encode() # Takes the password as user input and encodes it

genkey()            # This runs the function and writes the key to the key file
Key = loadkey()     # Loads the key and stores it in a variable
FE = Fernet(Key)    # Now we need to initialize or "activate" the Fernet object/key from the loadkey function. 

print("Encryption key generated, keep this to decrypt: " "\n", Key.decode(), "\n")        # Prints the key Generated. 

EncryptedPassword = FE.encrypt(Passwordinput)
print("Your Encrypted Password is: " , "\n", EncryptedPassword.decode(), "\n")  # Prints the encrypted password. 

#-------------------------------------------------------
# Now we will decrypt the string with the Fernet key we generated earlier. 
# 

DecKey = input("Enter Encryption Key to Decrypt password: ")
FD = Fernet(DecKey)      #Need to inialize DecKey with Fernet, similarly what we did earlier with "loadkey()"
EncPassword = input("Enter Encrypted Password to Decrypt: ")

DecPassword = FD.decrypt(EncPassword)
print("Your Decrypted Password is: " , "\n", DecPassword.decode(), "\n") 