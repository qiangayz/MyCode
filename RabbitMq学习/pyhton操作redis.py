import redis

r = redis.Redis(host='192.168.70.129',port=6379, password='1234')
r.set('name','zq')
print r.get('name')



#管道

