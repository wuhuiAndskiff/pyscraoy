"""
人人网cookie的使用
author：一叶扁舟
说明:使用的python3.7
"""
import  urllib.request


url = "http://www.renren.com/410043129/profile"

headers = {
"Accept" : "*/*",
"Accept-Language" : "zh-CN,zh;q=0.9",
"Connection" : "keep-alive",
"Content-Type" : "application/x-www-form-urlencoded",
 # "Cookie" :"xxxxxxxxxxxxxxxx",#将登陆人人网的的cookie直接复制过来
"Cookie" : "anonymid=jk57x9x8-5o63ht; depovince=FJ; jebecookies=7b1e127f-c865-432c-81f0-d648a6d0c7d9|||||; _r01_=1; JSESSIONID=abcP4YyKW1-dWc8TepGtw; ick_login=35106fcd-e565-41fc-bebc-c652f98ee29f; _de=50A108E895E0CCC9677B8FA35C706602; p=126f7a0cc92f629594d36f8826f2e1663; first_login_flag=1; ln_uact=wuwnho@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20121226/0040/h_main_GLzH_7b2200001d311376.jpg; t=9ebe303495b8a28a6b51edba1c00779c3; societyguester=9ebe303495b8a28a6b51edba1c00779c3; id=496371843; xnsid=1fc38483; loginfrom=syshome; jebe_key=6b8d9bf5-3ac0-49c9-a888-22987f210b9e%7Ce4d2baa9cbe935b22fadbf0138e278f2%7C1532770421388%7C1%7C1532770426471; wp_fold=0",
"Host" : "www.renren.com",
"Referer" : "http://www.renren.com/496371843/profile",
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"

}
request = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode("utf-8"))