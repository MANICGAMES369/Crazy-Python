import hashlib
import getpass

#Hashed based authentication by manicgames369

#publickey is the pre-hashed text

publickey="936a185caaa266bb9cbe981e9e05cb78cd732b0b3280eb944412bb6f8f8f07af"

password=getpass.getpass("Password:")
hashed1=hashlib.sha256(password.encode()).hexdigest()


if(hashed1==publickey):
    
    combine=hashlib.sha256(publickey+hashed1.encode()).hexdigest() #unique private keygenerate from 2 sha256 hashes
    print('Keep this private key safe: '+combine)

    del combine
    del hashed1
    del publickey
    del password

else:
    print("Incorrect password!")
