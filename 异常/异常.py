#coding=utf-8
names = ['a','b']
try:
    names[3]
# except IndexError as e:
#     print '123214',e

# except (KeyError,IndexError) as e:
#     print 'asdasd',e
#
except Exception as e:    #捕获所有异常，不建议用
     print '*******',e

else:                        #如果没出错会执行
    print '一切正常'

finally:
    print '不管有没有错都执行'

#自定义异常
class MyexceptionError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try :
    raise MyexceptionError('我的异常信息 ')
except MyexceptionError as e:
    print e