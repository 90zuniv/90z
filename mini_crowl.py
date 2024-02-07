# 뉴스 전체 크롤링 후 종목 분류
# ( 주요 키워드 찾기 -> 주요키워드가 한정된 종목 중 어느 종목과 유사성이 높은가 -> 종목찾기)

# selenium 패키지와 time 모듈 import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from gensim.summarization.summarizer import summarize
from transformers import pipeline

keyword= 'naver'
date= '2024-01-02'

url= "https://finance.naver.com/news/news_search.naver?rcdate=&q="+keyword+"&x=26&y=12&sm=all.basic&pd=4&stDateStart="+date+"&stDateEnd="+date
# url= "https://n.news.naver.com/article/449/0000267418"
# 크롬드라이버 실행
driver = webdriver.Chrome() 

#크롬 드라이버에 url 주소 넣고 실행
driver.get(url)
driver.maximize_window()
time.sleep(2)

sub= driver.find_elements(By.CLASS_NAME, "articleSubject")
# print('sub',sub)
for i in sub:
    # print('i: ',i)
    i.click()
    time.sleep(2)

    # news_ = driver.find_elements(By.ID, "newsct_article")
    # news_ = driver.find_elements(By.ID, "dic_area")

    news_ = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dic_area")))

    print('news_[0]',news_)
    print("!!!!!!!!!!!!!!!!!!!")
    ori_text= news_[0].text
    sum_text= summarize(ori_text)

    classifier = pipeline("sentiment-analysis", model="snunlp/KR-FinBert-SC")
    ori_cl = classifier(ori_text)
    sum_cl = classifier(sum_text)

    # print(ori_text)
    print(ori_cl)
    # print(sum_text)
    # print(sum_cl)
