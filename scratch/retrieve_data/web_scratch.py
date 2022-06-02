from bs4 import BeautifulSoup
import requests

url = "https://www.cnblogs.com/junglelk/p/15306514.html"

html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p')
print(first_paragraph.text)
first_paragraph_words = soup.find('p').text.split()
print(first_paragraph_words)

# 没有id会抛KeyError
first_paragraph_id = soup.find('p')['id']
# 没有id会返回None
first_paragraph_id2 = soup.find('p').get('id')
print(first_paragraph_id)
print(first_paragraph_id2)

# 更多的无演示的必要，可以参考官方文档
