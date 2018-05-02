import operator

urls = [
  "http://www.google.com/a.txt",
  "http://www.google.com.tw/a.txt",
  "http://www.google.com/download/c.jpg",
  "http://www.google.co.jp/a.txt",
  "http://www.google.com/b.txt",
  "https://facebook.com/movie/b.txt",
  "http://yahoo.com/123/000/c.jpg",
  "http://gliacloud.com/haha.png"
]

file_count = {}

for url in urls:
  file_name = url.split('/')[-1]
  if file_name in file_count:
    file_count[file_name] += 1
  else:
    file_count[file_name] = 1
    

sorted_by_count = sorted(file_count.items(), key=operator.itemgetter(1))

for i in range(1,4):
  name, count = sorted_by_count[-i]
  print('{} {}'.format(name, count))
