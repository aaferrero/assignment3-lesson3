'''
from Crypto.Cipher import DES


class MyDESCrypt:
    key = chr(11) + chr(11) + chr(11) + chr(11) + chr(11) + chr(11) + chr(11) + chr(11)
    iv = chr(22) + chr(22) + chr(22) + chr(22) + chr(22) + chr(22) + chr(22) + chr(22)

    def __init__(self, key='', iv=''):
        if len(key) > 0:
            self.key = key
        if len(iv) > 0:
            self.iv = iv

    def ecrypt(self, ecryptText):

            cipherX = DES.new(self.key, DES.MODE_CBC, self.iv)
            pad = 8 - len(ecryptText) % 8
            padStr = ""
            for i in range(pad):
                padStr = padStr + chr(pad)
            ecryptText = ecryptText + padStr
            x = cipherX.encrypt(ecryptText)
            return x.encode('hex_codec').upper()

            #return ""

    def decrypt(self, decryptText):
        try:

            cipherX = DES.new(self.key, DES.MODE_CBC, self.iv)
            str = decryptText.decode('hex_codec')
            y = cipherX.decrypt(str)
            return y[0:ord(y[len(y) - 1]) * -1]
        except:
            return ""

##des=MyDESCrypt()
#print(des.ecrypt('22222'))
#print(des.decrypt('duRRSh7HU4k='))


import binascii
from pyDes import des, CBC, PAD_PKCS5


def des_encrypt(s):
    """
    DES 加密
    :param s: 原始字符串
    :return: 加密后字符串，16进制
    """
    secret_key = '20171117'
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


def des_descrypt(s):
    """
    DES 解密
    :param s: 加密后的字符串，16进制
    :return:  解密后的字符串
    """
    secret_key = 'HyeyW130'
    iv = 'Hyey20100430'
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de


#str_en = des_encrypt('zx')
#str_en=str(input('明文：'))
#print(str_en)
str_en='XhkWNOPdLJA='
str_de = des_descrypt(str_en)
print(str_de)

import base64
strings=str(input('明文：'))
string=strings.encode("utf-8")
print(str(base64.b64encode(string))[2:-1])
import time
#time.sleep(60)
'''
from Cryptodome.Cipher import AES
from Cryptodome import Random
from binascii import b2a_hex,a2b_hex

# 要加密的明文
data=input('明文：')
#data = '南来北往'
# 密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.
# 目前AES-128足够用
key = b'15902152449 1989'
# 生成长度等于AES块大小的不可重复的密钥向量
iv = Random.new().read(AES.block_size)

# 使用key和iv初始化AES对象, 使用MODE_CFB模式
mycipher = AES.new(key, AES.MODE_CFB, iv)
# 加密的明文长度必须为16的倍数，如果长度不为16的倍数，则需要补足为16的倍数
# 将iv（密钥向量）加到加密的密文开头，一起传输
ciphertext = iv + mycipher.encrypt(data.encode())
#print(iv.type)
# 解密的话要用key和iv生成新的AES对象
#mydecrypt = AES.new(key, AES.MODE_CFB, ciphertext[:16])
# 使用新生成的AES对象，将加密的密文解密
#decrypttext = mydecrypt.decrypt(ciphertext[16:])
#print(a2b_hex(b2a_hex(ciphertext)))
#print('密钥k为：', key)
#print(ciphertext)
print(str(b2a_hex(ciphertext))[2:-1])
#print('密文1为：', b2a_hex(ciphertext)[:16])

#print('密文2为：', str(b2a_hex(ciphertext)[16:])[2:-1])
#print('解密后数据为：', decrypttext.decode())
import time
time.sleep(60)