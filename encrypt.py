from Cryptodome.Cipher import AES
from Cryptodome import Random
from binascii import b2a_hex,a2b_hex
'''
密文1为： c22388f151a38de0
密文2为： 0f9e31a3a9c912f6f8f262afbebc


'''

#iv=input('请输入密文1：')
#secret=input('请输入密文2：')
key = b'15902152449 1989'

#ciphertext=iv +secret
ciphertext=input('请输入密文：')
ciphertext=bytes(ciphertext, encoding = "utf8")
#print(ciphertext)
#ciphertext=str(b'\xba\xb8p\xf1x\xe5\x9d\xf3\xa1\xbd\xd3\xc9Z3\x10X3\xf1b\xfa')
ciphertext=a2b_hex(ciphertext)
#print(ciphertext)

#ciphertext= bytes(ciphertext, encoding = "utf8")
#print(b'\xba\xb8p\xf1x\xe5\x9d\xf3\xa1\xbd\xd3\xc9Z3\x10X3\xf1b\xfa')
#print(ciphertext)
mydecrypt = AES.new(key, AES.MODE_CFB, ciphertext[:16])
decrypttext = mydecrypt.decrypt(ciphertext[16:])
print('解密后数据为：', decrypttext.decode())