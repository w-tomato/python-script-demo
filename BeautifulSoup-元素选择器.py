from bs4 import BeautifulSoup

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
# soup = BeautifulSoup(h5Str)

# 打开文件
# soup = BeautifulSoup(open('index.html'))

# 指定解析器 (默认是html.parser)
soup = BeautifulSoup(h5Str, "lxml")

# 获取元素
print(soup.title)

# 获取元素的名称
print(soup.title.name)

# 获取元素的类型
print(type(soup.title))

# 获取元素的文本
print(soup.title.string)

# 当有多个相同的标签时，只会返回第一个
print(soup.p)

# 获取p标签的名称和名称类型
print(soup.p.name)
print(type(soup.p.name))

# 获取a标签的属性
print(soup.a.attrs)

# 获取head的子节点title
print(soup.head.title)

# 获取p的子节点（这里会返回一个列表）
print(soup.p.contents)
# 遍历p的子节点
for i in soup.p.contents:
    print(i)

# 获取p的子节点（这里会返回一个生成器）
print(soup.p.children)
# 遍历p的子节点
for i, child in enumerate(soup.p.children):
    print(i, child)

# 获取a的父节点
print(soup.a.parent)

# 获取a的祖先节点(返回一个生成器)
print(soup.a.parents)
# 遍历a的祖先节点
print(list(enumerate(soup.a.parents)))

# 获取a的后面的兄弟节点
print(soup.a.next_sibling)

# 获取a的后面的兄弟节点（这里会返回一个生成器）
print(soup.a.next_siblings)
# 遍历a的后面的兄弟节点
print(list(enumerate(soup.a.next_siblings)))

# 获取a的后面的所有兄弟节点
print(soup.a.p)

# 获取a的前面的所有兄弟节点（这里会返回一个生成器）
print(soup.a.previous_siblings)
# 遍历a的前面的所有兄弟节点
print(list(enumerate(soup.a.previous_siblings)))





