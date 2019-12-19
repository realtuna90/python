import bs4
import requests

# 달러 환율을 네이버 환율에서 가져오는 프로그램
html = requests.get('https://finance.naver.com/marketindex/?tabSel=worldExchange#tab_section')

soup = bs4.BeautifulSoup(html.text, 'html.parser')
dollar = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print(dollar.text)
