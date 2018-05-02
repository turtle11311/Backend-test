from bs4 import BeautifulSoup, SoupStrainer
import requests
import http.server
import socketserver

broad = 'Steam'

base_url = 'https://www.ptt.cc'
broad_url = base_url + '/bbs/{}/index.html'.format(broad)

session = requests.session()
response = session.get(broad_url)
page_content = response.text

article_list = SoupStrainer('div',{'id': 'main-container'})
tree = BeautifulSoup(page_content, 'html.parser', parse_only=article_list)

titles = tree.findAll('div', {'class': 'title'})
i = 0
for i in range(len(titles)):
  if titles[i].a == None:
    continue
  print("{}) {}".format(i, titles[i].text.strip()))

id = int(input('Select an article: '))

# Selected article URL
article_url = base_url + titles[id].a['href']
response = session.get(article_url)
article = response.text

article_content = SoupStrainer('div',{'id': 'main-content'})
article_tree = BeautifulSoup(article, 'html.parser', parse_only=article_content)

author, title, time = article_tree.select('div.article-metaline > span.article-meta-value')
author = author.text.strip()
title = title.text.strip()
time = time.text.strip()

print("作者：" + author)
print("標題：" + title)
print("時間：" + time)
print("內文：")
main = article_tree.select('div#main-content')[0]
print(main.text)
