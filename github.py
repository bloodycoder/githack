# -*- coding: utf-8 -*-
import urllib2,urllib,re
import time
class githack:
    def __init__(self):
        cookies = urllib2.HTTPCookieProcessor()
        self.opener = urllib2.build_opener(cookies)
        self.token =''
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'),('Origin','https://github.com'
                                    ),('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),('Accept-Language','zh-CN,zh;q=0.8'),
                                  ('Connection','keep-alive')]
        self.re_auth = re.compile('authenticity_token[^>]+') #得到github auth 信息
    def login(self,token,usr,password):
        self.formdata = {'commit':'Sign in','utf-8':'✓','authenticity_token':token,'login':usr,'password':password}
        data_encoded = urllib.urlencode(self.formdata)
        response = self.opener.open('https://github.com/session',data_encoded)
        print u'现在正在登陆',usr
    def view_login(self):
        response = self.opener.open('https://github.com/login/')
        html = response.read()
        auth = self.re_auth.findall(html)[0][41:-3]
        return auth
    def view_index(self):
        response = self.opener.open('https://github.com/')
        html = response.read()
        token = self.re_auth.findall(html)[0][41:-3]
        return token
    def logout(self,token):
        self.formdata = {'utf-8':'✓','authenticity_token':token}
        data_encoded = urllib.urlencode(self.formdata)
        response = self.opener.open('https://github.com/logout',data_encoded)
        print u'正在登出'
        print u'状态码为',response.getcode(),u'转到',response.geturl()
    def star(self,usrName,repoName):
        url = ''.join(['https://github.com/',usrName,'/',repoName,'/'])
        response = self.opener.open(url)
        html = response.read()
        token = self.re_auth.findall(html)[3][41:-3]
        formdata = {'utf-8':'✓','authenticity_token':token}
        data_encoded = urllib.urlencode(formdata)
        response = self.opener.open(url+'star',data_encoded)

def main(name,repo,num):
    f = open('acc3.txt','r')
    content = f.readline()
    cnt = 0
    while(len(content)>0):
        try:
            if(cnt>=num):
                return 0 
            content = eval(content)
            git = githack()
            token = git.view_login()
            git.login(token,content[0],content[1])
            git.star(name,repo)          
            token = git.view_index()
            git.logout(token)   
        except:
            content = f.readline()
            continue
        content = f.readline()
        cnt = cnt +1
        time.sleep(1)
    f.close()

main('bloodycoder','skeleton',600)
main('bloodycoder','pingke',100)
main('bloodycoder','Zhihu_craw',580)
main('bloodycoder','website_downloader',100)
main('bloodycoder','ideaBooster',80)
main('bloodycoder','VirtualTkinter',512)
"""
A = githack()
token = A.view_login()
A.login(token,'pighasa100','pighasa1')
A.star('bloodycoder','craw_books')
token = A.view_index()
A.logout(token)
"""
