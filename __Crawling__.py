import json
import requests as rq
from bs4 import BeautifulSoup
import time

keywords = ['GPT 3', 'GPT 4', 'ChatGPT']
lastPageNo = 1
result = []

for keyword in keywords:
    temp = []
    pageNo = 0
    for articleNo in range(0, (lastPageNo) * 10, 10):
        pageNo += 1
        print(f'============== Keyword : {keyword} / 페이지 : {pageNo} ==============')
        url = f"https://scholar.google.co.kr/scholar?start={articleNo}&q={keyword}&hl=ko&lr=lang_ko"
        res = rq.get(url)
        html = res.content.decode("utf-8")
        print(html)
        soup = BeautifulSoup(html, 'lxml')
        papers = soup.select('.gs_rt a')
        for paper in papers:
            print(paper)
            print(paper.getText())
            temp.append(paper.getText())
        time.sleep(10)
    result.append(temp)

with open('./result.json', 'w', encoding='euc-kr') as outfile:
    json.dump(result, outfile)

