# '''
# 문제) 16진수를 입력받아서 10진수로 출력하는 프로그램
# 첫째 줄에 16진수 최대 6글자
# 16진수는 0~9 : A~F
# '''

import sys
input = sys.stdin.readline
st = {'0':0,
    '1':1, 
    '2':2,
    '3':3, 
    '4':4, 
    '5':5, 
    '6':6, 
    '7':7, 
    '8':8, 
    '9':9, 
    'A':10, 
    'B':11, 
    'C':12, 
    'D':13, 
    'E':14, 
    'F':15}

text = list(input())
if len(text)-1 > 6:
    raise print("길이 초과, 6글자 내로 입력")

text   = text[:-1]
temp   = 0
result = 0
for i in text:
    if i in st.keys(): 
        result+=st[i]*(16**(len(text)-1-temp)) 
    temp = temp + 1

print(result)