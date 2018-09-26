import  urllib.request


url = "http://www.baidu.com/s"
# url = "http://www.python.org"
#
response = urllib.request.urlopen(url)
# print(response.read().decode("utf-8"))
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader("Server"))

print("-"*120)


# url = "http://httpbin.org/post"
dic = {"wd":"一叶扁舟"}
# data = urllib.urlencode(dic)
# 将did用utf-8格式编码，转成字节流
data = bytes(urllib.parse.urlencode(dic),encoding="utf8")
wd = "一叶扁舟"
# rep = urllib.request.urlopen(url,data=data)
# print(rep.read())
print("-"*120)
url = url + "?" +data;
headers = {'User-Agent':'Mozilla'}

request = urllib.request.urlopen(url ,headers=headers)
print(request.read())
