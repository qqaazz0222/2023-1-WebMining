# BeautifulSoup를 사용하여 구글 학술검색에서 논문 제목을 크롤링하는 코드입니다.
import json
import requests as rq
from bs4 import BeautifulSoup
import time

keywords = ["GPT 3", "GPT 4", "ChatGPT"]
lastPageNo = 10
result = []

for keyword in keywords:
    temp = []
    pageNo = 0
    for articleNo in range(0, (lastPageNo) * 10, 10):
        pageNo += 1
        print(f"============== Keyword : {keyword} / 페이지 : {pageNo} ==============")
        url = f"https://scholar.google.co.kr/scholar?start={articleNo}&q={keyword}&hl=ko&lr=lang_ko"
        res = rq.get(url)
        try:
            html = res.content.decode("euc-kr")
            soup = BeautifulSoup(html, "lxml")
            papers = soup.select(".gs_rt a")
            for paper in papers:
                title = f"{paper.text}"
                print(title)
                # temp.append(title)
                result.append(title)
        except:
            print("error!")
            html = res.content.decode("utf-8")
            print(html)
        time.sleep(5)
    # result.append(temp)

with open("./CrawlingRes.json", "w", encoding="utf-8") as outfile:
    json.dump(result, outfile, ensure_ascii=False)
