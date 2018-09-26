"""
爬取ajax数据--豆瓣网
author:一叶扁舟
说明:使用的python3.7
"""

import urllib
import urllib.request


url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

formdata = {
        "start":"0",
        "limit":"100"
    }

data = urllib.parse.urlencode(formdata).encode("utf-8")

request = urllib.request.Request(url, data = data, headers = headers)

print (urllib.request.urlopen(request).read().decode("utf-8"))




