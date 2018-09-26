"""
json字符串学习
@author:一叶扁舟
loads :将字符串转成json对象

"""
import json
strList = '[1, 2, 3, 4]'
strDict = '{"city": "北京", "name": "大猫"}'
print(json.loads(strList))
numList = json.loads(strList)
for num in numList:
    print(num)
print(json.loads(strDict))
print(type(strList))
print(type(strDict))