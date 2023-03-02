
from Crypto.Cipher import AES
class Distruct:
    def __init__(self):
        
        self.key =  'password_1234567'.encode("utf8")
        self.salt = '2c13f9e844be4b93'.encode("utf8")

        
    def content(self,payload, block_size=16):
        self.payload = payload
        self.length = block_size - (len(self.payload) % block_size)
        data =  self.payload + chr(self.length) * self.length 
        return data.encode("utf8")

    def encrypt(self):
        self.obj = AES.new(self.key, AES.MODE_CBC, self.salt).encrypt(self.content("1"))
        print(self.obj)
    
    def decrypt(self):
        self.dec = AES.new(self.key, AES.MODE_CBC, self.salt).decrypt(self.obj)
        print(int(str(self.dec.decode("utf-8"))[:1]))

        
conver = Distruct()
conver.content("input content")
conver.encrypt()
conver.decrypt()
# ----------------------------------------------------------------------



# f = open("own.txt","r")
# val = int(f.read())
# val +=1
# f.close()

# f = open("own.txt","w")
# f.write(str(val))
# print("----------> ",val)
# f.close()