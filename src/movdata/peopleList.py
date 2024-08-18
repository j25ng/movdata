import requests
import os
import json
import time
from tqdm import tqdm

API_KEY = os.getenv('MOVIE_API_KEY')

def save_json(data, file_path):
    # 파일저장 경로
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def req(url):
    r = requests.get(url).json()
    return r

def save_people(per_page=10, sleep_time=1):
    file_path = f'data/movies/people/peopleList.json'
    
    # 위 경로가 있으면 API 호출을 멈추고 프로그램 종료
    if os.path.exists(file_path):
        print(f"데이터가 이미 존재합니다: {file_path}")
        return True

    # totCnt 가져와서 total_pages 계산
    url_base = f"https://kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={API_KEY}"
    r = req(url_base + "&curPage=1")
    #tot_cnt = r['peopleListResult']['totCnt']
    #total_pages = (tot_cnt // per_page) + 1
    # 100페이지까지만 저장해보기
    total_pages = 1000

    all_data = []
    # total_pages 만큼 Loop 돌면서 API 호출
    for page in tqdm(range(1, total_pages + 1)):
        time.sleep(sleep_time)
        r = req(url_base + f"&curPage={page}")
        d = r['peopleListResult']['peopleList']
        all_data.extend(d)

    save_json(all_data, file_path)
    return True
