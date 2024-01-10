from bs4 import BeautifulSoup

html = """
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class-"list" id="list-1">
<li class-"element"> Foo</li>
<li class="element">Bar</li> 
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element"> Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
"""

soup = BeautifulSoup(html, 'lxml')

# 获取panel-heading的div
# print(soup.select(".panel .panel-heading"))

# # 获取所有的li节点
# print(soup.select("li"))
# # 获取所有的li节点通过class
# print(soup.select(".element"))

# # 获取id为list-2的ul节点
# print(soup.select("#list-2"))

# 嵌套选择：

# 获取id为list-2的ul节点下的所有li节点
for ul in soup.select("ul"):
    for li in ul:
        print(li)

# find_all()用法
print(soup.find_all(name="ul"))

# 用正则表达式来匹配
import re
reg = re.compile("^l")
print(soup.find_all(name=reg))

# name的列表用法
print(soup.find_all(name=["ul", "li"]))

# True的用法（会匹配所有的标签）
print(soup.find_all(name=True))

# 查找class属性为"sidebar"的<div>标签
print(soup.find_all('div', attrs={'class': 'panel-body'}))
