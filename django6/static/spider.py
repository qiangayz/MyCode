#coding=utf-8
import requests
session = requests.session()
#获取图片
cap_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.19462885619731285'
respons = session.get(cap_url)
print respons.content
f= open('test.jpg','wb')
f.write(respons.content)
f.close()
#检查验证码
check_url='https://kyfw.12306.cn/passport/captcha/captcha-check'
code = raw_input('请输入坐标：')
data = {
'answer': code.split(),
'login_site': 'E',
'rand': 'sjrand',
}
check_respons_obj = session.post(check_url,data)
checkresult=  check_respons_obj.json()
print checkresult
#判断登录状态
login_url = 'https://kyfw.12306.cn/passport/web/login'
login_data = {
'username': 'qiangayz@163.com',
'password': 'ayz0804',
'appid': 'otn',
}
res = session.post(login_url,data=login_data)
print res.text