import  http.cookiejar, urllib.request,urllib.error


url = "http://localhost:9999/alipayDemoJava/"
cookies = http.cookiejar.CookieJar();
handler = urllib.request.HTTPCookieProcessor(cookies);
opener = urllib.request.build_opener(handler)
response = opener.open(url)

for item in cookies:
    print(item.name + "=" +item.value)




print("-"*120)

filename = "cookies.txt"
cookie = http.cookiejar.MozillaCookieJar(filename);
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
res = opener.open(url)
cookie.save(ignore_discard=True, ignore_expires=True)


print("-"*120)
baidu = "http://www.baidu.com"
try:

    res = opener.open(baidu)
except urllib.error.URLError as e:
    print(e.reason)
    print("这个url不能访问")