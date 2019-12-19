# 명단에서 이름을 뽑아서 영어소개와 한글소개
import random

name = ['홍길동','희동이','둘리']
eng_name = {
    '홍길동':'Hong','희동이':'Dong','둘리':'Twolee'
}

지목된사람 = random.choice(name)
지목된영어이름 = eng_name[지목된사람]

# 저는 홍길동입니다. My name is Hong
han_intro = '저는 ' + 지목된사람 + '입니다.'
eng_intro = ' My name is ' + 지목된영어이름
intro = han_intro + eng_intro

intro2 = '저는 {}입니다. My name is {}'.format(지목된사람, 지목된영어이름)

intro3 = f'저는 {지목된사람}입니다. My name is {지목된영어이름}'

print(intro)
print(intro2)
print(intro3)

