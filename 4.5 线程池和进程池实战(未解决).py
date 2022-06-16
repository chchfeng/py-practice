# 1. 如何提取单个页面的数据
# 2. 上线程池，多个页面同时抓取
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import asyncio
import aiohttp
import aiofiles
import json

def getPrice(url):
    resp = requests.get(url)
    dic = resp.json()
    for prices in dic['list']:
        prodCat = prices['prodCat']
        prodName = prices['prodName']
        lowPrice = prices['lowPrice']
        avgPrice = prices['avgPrice']
        highPrice = prices['highPrice']
        specInfo = prices['specInfo']
        place = prices['place']
        unitinfo = prices['unitInfo']
        pubDate = prices['pubDate']
        print(prodCat, prodName, lowPrice, avgPrice, highPrice, specInfo, place, unitinfo, pubDate)

if __name__ == '__main__':
    getPrice("http://www.xinfadi.com.cn/getPriceData.html")

