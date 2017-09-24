from bs4 import BeautifulSoup
import requests
import time

url_saves = 'http://www.tripadvisor.com/Saves#37685322'
url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
urls = ['https://cn.tripadvisor.com/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,930,30)]

headers = {
    'User-Agent':' ',
    'Cookie':' ',
}


def get_attractions(url,data=None):
    wb_data = requests.get(url)
    time.sleep(4)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles    = soup.select('div.property_title > a[target="_blank"]')
    imgs      = soup.select('img[width="160"]')  #事实上这样写并不行，因为图片基本根据js加载，可以用Chrome切换到app模式，将header下的user-Agent 改为移动端的 
    cates     = soup.select('div.p13n_reasoning_v2')
    if data == None:
        for title,img,cate in zip(titles,imgs,cates):
            data = {
                'title'  :title.get_text(),
                'img'    :img.get('src'),
                'cate'   :list(cate.stripped_strings),
                }
        print(data)


def get_favs(url,data=None):
    wb_data = requests.get(url,headers=headers)
    print(wb_data)
    soup      = BeautifulSoup(wb_data.text,'lxml')
    titles    = soup.select("div.title.titleLLR > div")
    imgs      = soup.find_all("div", "missing lazyMiss")
    metas     = soup.select('div.attraction_types > span')
    
    if data == None:
        for title,img,meta in zip(titles,imgs,metas):
            data = {
                'title'  :title.get_text().strip(),
                'img'    :img.get('data-thumburl'),
                'meta'   :meta.get_text()
            }
            print(data)

for single_url in urls:
    get_attractions(single_url)


# from mobile web site
'''
headers = {
    'User-Agent':'', #mobile device user agent from chrome
}


mb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(mb_data.text,'lxml')
imgs = soup.select('div.thumb.thumbLLR.soThumb > img')
for i in imgs:
    print(i.get('src'))
'''
