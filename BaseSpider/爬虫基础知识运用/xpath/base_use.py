"""
xpath基本语法的使用

"""

from lxml import  etree

html = """
<li class = "item-0"> <a href="link1.html">firset item</a></li>
<li class = "item-1"> <a href="link2.html">second item</a></li>
<li class = "item-inactive"> <a href="link3.html">third item</a></li>
<li class = "item-1"> <a href="link4.html">fourth item</a></li>
<li class = "item-0"> <a href="link5.html">fifth item</a></li>
"""

text = etree.HTML(html)
result = etree.tostring(text)
print(result.decode('utf-8'))