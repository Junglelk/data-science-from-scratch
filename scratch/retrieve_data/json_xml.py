import json

from bs4 import BeautifulSoup

serialized = """{"title": "Data Science Book", "author": "John Grus", "publicationYear": "2019","topics": ["data science", "machine learning", "artificial intelligence"]}"""

# 将json反序列化成python对象
deserialized = json.loads(serialized)
assert deserialized["title"] == "Data Science Book"
assert deserialized["author"] == "John Grus"
assert deserialized["publicationYear"] == "2019"
print("done")

#
xml_txt = """<Book>
    <title>Data Science Book</title>
    <author>John Grus</author>
    <publicationYear>2019</publicationYear>
    <topics>
        <topic>data science</topic>
        <topic>machine learning</topic>
        <topic>artificial intelligence</topic>
    </topics>
</Book>"""

beautiful_soup = BeautifulSoup(xml_txt, "xml")  # 看文档上应该是这么写的，但实际会报错，不清楚原因 -> 需要安装lxml
print(beautiful_soup.find("title").text)
