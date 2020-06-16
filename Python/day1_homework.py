import requests
import re
from lxml import etree

"""
    day1作业:
     爬取猫眼前七页的预告片
"""

url1 = 'https://maoyan.com/news?showTab=3&offset=0'
url2 = 'https://maoyan.com/news?showTab=3&offset=16'
url3 = 'https://maoyan.com/news?showTab=3&offset=32'
url4 = 'https://maoyan.com/news?showTab=3&offset=48'
url5 = 'https://maoyan.com/news?showTab=3&offset=64'
url6 = 'https://maoyan.com/news?showTab=3&offset=80'
url7 = 'https://maoyan.com/news?showTab=3&offset=96'

ua = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

"""result = requests.get(url1,headers=ua).content.decode()
dom = etree.HTML(result)
urls = dom.xpath('//ul[@class="list-pager"]/li/a[@href]/@href')
print(urls)"""

#方法get_movie()用于获取视频的源地址并下载到movie文件夹里
def get_movie(url,ua):
    result = requests.get(url,headers=ua).content.decode()

    dom = etree.HTML(result)
    movie_names = dom.xpath('//h4[@class="video-name one-line"]/a[@href]/text()')
    movie_urls = dom.xpath('//h4[@class="video-name one-line"]/a[@href]/@href')

    for movie_name,movie_url in zip(movie_names,movie_urls):
        movie_url_str = requests.get(movie_url).text

        movie_mp4 = re.search('source src="(.*)" type="video/mp4"', movie_url_str).group(1)
        print(movie_mp4)

        mp4 = requests.get(movie_mp4).content
        with open('./movie/%s.mp4'%movie_name,'wb') as file:
            file.write(mp4)

"""get_movie(url1,ua)
get_movie(url2,ua)
get_movie(url3,ua)
get_movie(url4,ua)
get_movie(url5,ua)
get_movie(url6,ua)
get_movie(url7,ua)"""
