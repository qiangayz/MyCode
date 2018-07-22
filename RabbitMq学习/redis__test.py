import redis
r = redis.Redis(host='192.168.70.129',port=6379, password='123456')
r.set('name','zq')
print r.get('name')
print r.get('name1')
