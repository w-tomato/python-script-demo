# 导入包
from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Chrome("/Users/corleone/projects/chromedriver")    # Chrome浏览器
# 打开网页
driver.get("www.google.com") # 打开url网页 比如 driver.get("http://www.baidu.com")

# 打开字符串
h5Str = """
<html><head><title>这是一个测试</title></head>
<body>
<a href='www.baidu.com' class='good' id='first'>haha</a>
<a href='www.baidu.com' class='good2' id='first2'>haha2</a>
<h1>这是一个标题</h1>
<p>这是一个段落
<a href='www.baidu.com' class='perfect' id='second'>hehe</a>
<a href='www.baidu.com' class='nice' id='third'>aoao</a>
</p>
<p>这是第二个段落</p>
</body></html>"
"""
# 直接解析字符串
# soup = BeautifulSoup(h5Str)

# 打开文件
# soup = BeautifulSoup(open('index.html'))

# 指定解析器 (默认是html.parser)
# soup = BeautifulSoup(h5Str, "lxml")

# 访问地址127.0.0.1:9528 解析这个网页
soup = BeautifulSoup(open('http://127.0.0.1:9528'))

# 获取元素
print(soup.title)

# 其他各种方法随用随看吧，很简单，这里记一下find_all()方法的使用

# 使用 name 参数查找指定标签名的元素
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.text)

# 使用 attrs 参数查找具有指定属性和属性值的元素
divs = soup.find_all(attrs={'class': 'content'})
for div in divs:
    print(div.text)

# 使用 text 参数查找具有指定文本内容的元素
h1 = soup.find_all(text='Title')
print(h1)

# 使用 limit 参数限制返回的元素数量
limited_divs = soup.find_all('div', limit=1)
for div in limited_divs:
    print(div.text)

# 使用 recursive 参数控制是否递归查找子孙元素
div = soup.find('div')
children = div.find_all('p', recursive=False)
for child in children:
    print(child.text)

# find()和find_all()都是BeautifulSoup库中用于查找元素的方法，它们的区别在于返回的结果类型和数量。
# find(name, attrs, recursive, text, **kwargs)`方法用于查找满足指定条件的第一个元素，并返回该元素。如果找不到符合条件的元素，它将返回`None`。
# find_all(name, attrs, recursive, text, limit, **kwargs)`方法用于查找满足指定条件的所有元素，并返回一个包含这些元素的列表。如果找不到符合条件的元素，它将返回一个空列表。

# 使用 find() 方法查找第一个符合条件的元素
paragraph = soup.find('p')
print(paragraph.text)