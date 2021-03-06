"""
通过post提交，访问有道翻译，得到翻译的数据
author:一叶扁舟
说明:使用的python3.7
"""

import urllib
import urllib.request
# 通过抓包的方式获取的url，并不是浏览器上显示的url,或者谷歌浏览器打开开发则调试工具，查看访问请求
# url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc"

# 完整的headers
headers = {
        "Accept" : "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With" : "XMLHttpRequest",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
    }

# 用户接口输入
key = input("请输入需要翻译的文字:")

# 发送到web服务器的表单数据
formdata = {
"type" : "AUTO",
"i" : key,
"doctype" : "json",
"xmlVersion" : "1.8",
"keyfrom" : "fanyi.web",
"ue" : "UTF-8",
"action" : "FY_BY_CLICKBUTTON",
"typoResult" : "true"
}

# 经过urlencode转码
# 如果报错了:出现了“POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.”则需要在后面添加.encode(encoding='UTF8')
data = urllib.parse.urlencode(formdata).encode(encoding='UTF8')

# print(data)
# 如果Request()方法里的data参数有值，那么这个请求就是POST
# 如果没有，就是Get
request = urllib.request.Request(url, data = data, headers = headers)

print(urllib.request.urlopen(request).read().decode("utf-8"))

