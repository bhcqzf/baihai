def download_one(url):
    import requests
    from bs4 import BeautifulSoup
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    demo = r.text
    # print(r.text)
    soup = BeautifulSoup(demo, 'lxml')
    # print(soup.prettify())
    booktitle = soup.select('#wrapper > div.content_read > div > div.con_top > a')[-1].text
    # print(booktitle)
    title = soup.find('div', class_='bookname').h1.text
    print('正在下载  '+booktitle+title)
    txts = soup.find_all('div', id="content")
    for txt in txts:
        txt1 = txt.text
        with open(booktitle + '.txt', 'a', encoding='utf-8') as f:
            # print(txt1)
            f.write(title + '\n')
            f.write(txt1 + '\n' + '\n')
    pass

'''
import requests
from lxml import etree

header={'User-Agent': 'Mozilla/5.0'}
r=requests.get('http://www.xbiquge.la/10/10489/',headers=header)
r.encoding=r.apparent_encoding
demo=r.text
# print(demo)
demo=etree.HTML(r.text)
urls=demo.xpath('//*[@id="list"]/dl')
for url in urls:
    url1=url
    print(url1)
# for url in urls:
# #     # download_one('http://www.xbiquge.la/10/10489/'+url)
#         print(url)
# #     # print('http://www.xbiquge.la/10/10489/'+url)
#
'''


def download_one_book(url):
    import requests
    from bs4 import BeautifulSoup
    header={'User-Agent': 'Mozilla/5.0'}
    r=requests.get(url,headers=header)
    r.encoding=r.apparent_encoding
    soup=BeautifulSoup(r.text,'lxml')
    # print(soup.prettify())
    urls=soup.select("#list > dl > dd > a")
    for url1 in urls:
        # print(url1)
        url2=url1.get('href')
        urlzz=('http://www.xbiquge.la'+url2)
        download_one(urlzz)
    pass

# url=input('请输入要下载小说的目录网址:')
# url1=str(url)
# download_one_book(url1)
# print(url1)
if _name_='_main_':
    download_one_book('http://www.xbiquge.la/1/1690/')   //此处输入要下载小说目录的链接
