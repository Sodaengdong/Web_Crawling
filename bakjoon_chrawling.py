from urllib.request import Request, urlopen
import urllib.parse
from bs4 import BeautifulSoup   
#BeautifulSoup 클래스는 웹문서를 파싱하여, 크롤링을 할 수 있게 문서 개체를 생성해준다

#웹페이지에 접근
with urllib.request.urlopen('https://www.acmicpc.net/problemset/1') as response:
    #html 코드 가져오기
    html = response.read()
    soup = BeautifulSoup(html,'html.parser') 

    #대상 선택
    answerrate = soup.select('tbody tr td:nth-child(6)')
    sum = 0
    for text in answerrate:
        print(text.text[0:-1]) #float형 정답율 데이터만 추출하기 위해 '%' cut
        sum += float(text.text[0:-1]) #합계
    length = len(answerrate)
    acp = round(sum/(len(answerrate)),3) #평균을 소수 셋째 자리까지 표시
    print('Size='+str(length))
    print('Average Correct Percentage='+str(acp)+'%')
    
