# 1. replace
# 문자열 교체
a='오늘 날씨는 흐림 입니다.'.replace("흐림", "맑음")
print(a)

# 2. find
# 문자열 찾기
b = 'hello world'.find("w2orld")
print(b)

# 3. split
# 문자열 분리
c = '나이키신발 265 ㅇㄹㅇ ㅇㄹㅇㄹㅇ'.split()
print(c)

d = '나이키신발 :265 ㅇㄹㅇ :ㅇㄹㅇㄹㅇ'.split(':')
print(d)

# 4. strip
# 문자열 공백 제거
e= '          ㅛ교  '.strip()
print(e)