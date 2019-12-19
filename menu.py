# 랜덤으로 오늘의 점심메뉴를 추천해주는 프로그램
import random

menu = ['새마을식당', '초원삼겹살', '멀캠20층', '홍콩반점', '순남시래기']

phone_book = {
    '새마을식당':'010-1234-1123',
    '초원삼겹살':'02-000-0012',
    '멀캠20층':'02-856-4441',
    '홍콩반점':'02-225-3221',
    '순남시래기':'02-111-2222'
}

# print(phone_book['새마을식당'])

# menu의 요소 중 랜덤으로 골라서 lunch라고 하는 변수에 담아주세요
# 실습 : 랜덤으로 고른 식당과 해당식당의 전화번호를 출력
lunch = random.choice(menu)
print(lunch)
print(phone_book[lunch])