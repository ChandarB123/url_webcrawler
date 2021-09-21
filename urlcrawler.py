from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import random
import time


def valid_url(url):
    parsed = urlparse(url)
    if parsed.scheme == "http" or parsed.scheme == "https":
        return True
    else:
        return False

def crawl(starting_site):
    if valid_url(starting_site):
        print("Crawling... " + starting_site)
        r = requests.get(starting_site, headers={'User-Agent': header_rand}, proxies={"http": proxy_rand, "https": proxy_rand})
        page = BeautifulSoup(r.text, 'html.parser')
        all_links = page.find_all('a')
        for link in all_links:
            links = link.get("href")
            if valid_url(links):
                if links not in visited:
                    queue.append(links)

queue = []
visited = set()

header_list = [
    'Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)',
    'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)'
]
header_rand = random.choice(header_list)

proxy_list = [
    '106.54.219.223:8888',
    '91.192.4.162:8090',
    '88.99.10.251:1080',
    '110.249.176.26:8060'
]
proxy_rand = random.choice(proxy_list)

starting_url = input("Enter the starting url: ")
crawl(starting_url)
for i in queue:
    crawl(i)
    visited.add(i)
    time.sleep(random.randint(1, 5))

print(queue, visited)
