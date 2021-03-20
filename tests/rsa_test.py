# -*- coding:UTF-8 -*-
__author__ = 'rxz'

import rsa


# rsa加密
def rsaEncrypt(str):
    # 生成公钥、私钥
    (pubkey, privkey) = rsa.newkeys(512)
    print("pub: ", pubkey)
    print("priv: ", privkey)
    # 明文编码格式
    content = str.encode('utf-8')
    # 公钥加密
    crypto = rsa.encrypt(content, pubkey)
    return (crypto, privkey)


# rsa解密
def rsaDecrypt(str, pk):
    # 私钥解密
    content = rsa.decrypt(str, pk)
    con = content.decode('utf-8')
    return con


(a, b) = rsaEncrypt("hello")
print('加密后密文：')
print(a)
content = rsaDecrypt(a, b)
print('解密后明文：')
print(content)
"""
————————————————
版权声明：本文为CSDN博主「阿紫_PP」的原创文章，遵循CC
4.0
BY - SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https: // blog.csdn.net / ruanxingzi123 / article / details / 83017575
"""