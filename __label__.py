# 라벨링 데이터를 분석하여 엑셀로 저장하는 코드
import json
from collections import Counter

import pandas as pd

res = Counter()

with open("./labeldata.json", "r") as f:
    loadData = json.load(f)
    # print(loadData)
    for data in loadData:
        data = Counter(data)
        for key in data:
            res[key] += data[key]

temp = 0
for key in res:
    temp += res[key]
# print(res, temp)

labelDict = {
    "A": "농업, 임업 및 어업",
    "B": "광 업",
    "C": "제 조 업",
    "D": "전기, 가스, 증기 및 공기 조절 공급업",
    "E": "수도, 하수 및 폐기물 처리, 원료 재생업",
    "F": "건 설 업",
    "G": "도매 및 소매업",
    "H": "운수 및 창고업",
    "I": "숙박 및 음식점업",
    "J": "정보통신업",
    "K": "금융 및 보험업",
    "L": "부동산업",
    "M": "전문, 과학 및 기술 서비스업",
    "N": "사업시설 관리, 사업 지원 및 임대 서비스업",
    "O": "공공 행정, 국방 및 사회보장 행정(84)",
    "P": "교육 서비스업",
    "Q": "보건업 및 사회복지 서비스업",
    "R": "예술, 스포츠 및 여가관련 서비스업",
    "S": "협회 및 단체, 수리 및 기타 개인 서비스업",
    "T": "가구 내 고용활동 및 달리 분류되지 않은 자가 소비 생산활동",
    "U": "국제 및 외국기관",
}

classificiation = []
workLabel = []
values = []

for k, v in res.items():
    classificiation.append(k)
    workLabel.append(labelDict[k.upper()])
    values.append(v)
frame = pd.DataFrame({"구분": classificiation, "업종": workLabel, "개수": values})

frame.to_excel(excel_writer="label.xlsx")
