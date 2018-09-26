

#
# from   scrapy.cmdline import execute
# import os
# import  sys
# #当前文件名
# filePath = os.path.abspath(__file__)
# #当前文件的所在的文件夹
# fileDir = os.path.dirname(filePath)
# print(filePath)
# print(fileDir)
#
# sys.path.append(fileDir)
# execute(['scrapy','crawl','jobbole'])



from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "jobbole"])