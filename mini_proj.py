# 뉴스 전체 크롤링 후 종목 분류
# ( 주요 키워드 찾기 -> 주요키워드가 한정된 종목 중 어느 종목과 유사성이 높은가 -> 종목찾기)

# selenium 패키지와 time 모듈 import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from gensim.summarization.summarizer import summarize

url= "https://n.news.naver.com/article/449/0000267418"

# 크롬드라이버 실행
driver = webdriver.Chrome() 

#크롬 드라이버에 url 주소 넣고 실행
driver.get(url)

time.sleep(1)

news_ = driver.find_elements(By.ID, "newsct_article")

# for i in news_:
#     title = i.text
#     print(title)

# print("lllll",news_)

text= news_[0].text
print(summarize(text))