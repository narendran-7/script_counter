
from Crypto.Cipher import AES
class Distruct:
    def __init__(self):
        
        key =  'password_1234567'.encode("utf8")
        salt = '2c13f9e844be4b93'.encode("utf8")

        obj = AES.new(key, AES.MODE_CBC, salt).encrypt(self.content("payload"))
        print(obj)
        
    def content(self,payload, block_size=16):
        length = block_size - (len(payload) % block_size)
        data =  payload + chr(length) * length 
        return data.encode("utf8")


conver = Distruct()
conver.content("input content")


# ----------------------------------------------------------------------



# f = open("own.txt","r")
# val = int(f.read())
# val +=1
# f.close()

# f = open("own.txt","w")
# f.write(str(val))
# print("----------> ",val)
# f.close()