#coding=utf-8
import ConfigParser  #配置文件模块
import hashlib    #用于加密的模块
m = hashlib.md5()
m.update(b'hello')
print m.hexdigest()

m.update(b'i am  oung ')
print m.hexdigest()

m1 = hashlib.sha1()
m1.update(b'hello')
print m1.hexdigest()

m1.update(b'i am  oung ')
print m1.hexdigest()

import hmac
h = hmac.new(b'234234','asdasd')
print h.digest()
print h.hexdigest()