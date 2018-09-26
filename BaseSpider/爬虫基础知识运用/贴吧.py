"""
爬取百度贴吧的内容
@author:一叶扁舟
"""
import urllib.request
import urllib




def loadPage(fullUrl, filName):
    """
    加载页面
    :return:
    """
    print("正在下载......"+filName+".....")

    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}

    request = urllib.request.Request(fullUrl,headers = headers)

    return urllib.request.urlopen(request).read()




def writePage(html,fileName):
    # print(html)
    """
    将页面写到磁盘
    :return:
    """
    with open("./spiderhtml/"+fileName,"wb") as f:
        f.write(html)
        print("-"*120)





def baiduTiebaSpider(url,startNum,endNum):
    """
    组装拼接的url
    :return:
    """
    for page in range(startNum, endNum+1):
        # 页数
        pn = (page  - 1) * 50
        # //将一页的数据保存下来
        fileName = "第"+str(page)+"页.html"

        # 加页数的访问路径
        fullUrl = url +"&pn=" + str(pn)

        html = loadPage(fullUrl, fileName)

        writePage(html,fileName)



if __name__ == "__main__":
    kw = input("请输入关键词:")
    startNum = int(input("请输入起始页:"))
    endNum = int(input("请输入结束页:"))
    dic = {"kw":kw}

    url = "http://tieba.baidu.com/f?"
    key =  urllib.parse.urlencode(dic)
    fullUrl = url + key

    baiduTiebaSpider(fullUrl,startNum,endNum)

