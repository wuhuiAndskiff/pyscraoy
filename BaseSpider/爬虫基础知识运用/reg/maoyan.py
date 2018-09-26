import  requests
import re
import json
import time



#对爬取的一个页面利用正则进行解析
def parse_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    resultList = re.findall(pattern,html)
    #利用正则提取数据到python实体中
    for item in resultList:
        yield{
            'index':item[0],
            'image':item[1],
            "title":item[2],
            "actor":item[3].strip()[3:],
            "time":item[4].strip()[5:],
            "score":item[5]+item[6],
        }


#爬取一个网页
def get_one_printpage(url):
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0"}

        response = requests.get(url,headers=headers)
        if(response.status_code == 200):
            return response.text
    except Exception:
        return None
#将爬取的数据写入文件中
def write_to_file(result):
    with open("result.txt","a",encoding="utf-8")as f:
        f.write(json.dumps(result,ensure_ascii=False))+'\n'

def crawler(offset):
    url = "http://maoyan.com/board/4?offset="+str(offset)
    html = get_one_page(url)
    print(html)
    for item in parse_page(html):
        print(item)
        write_to_file(item)

if __name__ == "__main__":
    for i in range(10):
        crawler(i*10)
        time.sleep(1)
