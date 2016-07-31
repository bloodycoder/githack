# -*- coding: utf-8 -*-
import urllib2,urllib,re
import time
class gitjoin:
    def __init__(self):
        cookies = urllib2.HTTPCookieProcessor()
        self.opener = urllib2.build_opener(cookies)
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'),('Origin','https://github.com'
                                    ),('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),('Accept-Language','zh-CN,zh;q=0.8'),
                                  ('Connection','keep-alive')]
        self.re_auth = re.compile('authenticity_token[^>]+') #得到github auth 信息
    def view(self):
        response = self.opener.open('https://github.com/join')
        html = response.read()
        print u'正在登录join'
        print u'状态码为',response.getcode()
        token = self.re_auth.findall(html)[0][41:-3]
        return token
    def view_index(self):
        response = self.opener.open('https://github.com/')
        html = response.read()
        token = self.re_auth.findall(html)[0][41:-3]
        return token
    def zhuce(self,token,login,email,password):
        self.formdata = {'utf-8':'✓','authenticity_token':token,'user[login]':login,'user[email]':email,'user[password]':password,'source':'form-home'}
        data_encoded = urllib.urlencode(self.formdata)
        print data_encoded
        response = self.opener.open('https://github.com/join',data_encoded)
        print u'正在注册'
        print u'状态码为',response.getcode(),u'转到',response.geturl()
    def logout(self,token):
        self.formdata = {'utf-8':'✓','authenticity_token':token}
        data_encoded = urllib.urlencode(self.formdata)
        response = self.opener.open('https://github.com/logout',data_encoded)
        print u'正在登出'
        print u'状态码为',response.getcode(),u'转到',response.geturl()
#githacker = githack()
def main():
    name = 'xjaiswjh'
    email = ''
    password = 'pighasa1'
    f = open('acc.conf','w')
    signin = gitjoin()
    for i in range(80000,81000):
        newname = name+str(i)
        email = newname + '@qq.com'
        print u'现在正在注册',newname
        to_write = ''.join(['(','"',newname,'"',',','"',password,'"',')','\n'])
        try:
            token = signin.view()
            signin.zhuce(token,newname,email,password)
            token = signin.view_index()
            signin.logout(token)
            f.write(to_write)
        except:
            print newname,u'失败'
        print '*****************'
        print '*****************'
        time.sleep(1)
    f.close()
main()
