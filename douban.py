import requests
import json

'''
豆瓣热门电视剧简单爬虫
'''
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
r = requests.get("https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0",headers=headers)
resp = r.json()

# 将获取的电视剧信息放入文件中
filename = '.\\file\\HotTV.csv'
with open(filename,"a",encoding="utf-8") as f:
    for sub in resp["subjects"]:
        hotTV = "剧名：《{0}》,评分：{1},观看地址：{2}\n".format(sub["title"],sub["rate"],sub["url"])
        f.write(hotTV)