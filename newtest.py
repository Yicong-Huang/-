
import urllib.request  
res=urllib.request.urlopen('http://www.baidu.com')  
htmlBytes=res.read()  
print(htmlBytes.decode('utf-8'))