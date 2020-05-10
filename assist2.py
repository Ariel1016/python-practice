import numpy as np

#2
pin="990329-1083599"
YYYY=pin[0:2]
MM=pin[2:4]
DD=pin[4:6]
print("김멋사군의 탄생일은 19%s년 %s월 %s입니다." %(YYYY,MM,DD), end="")

#3
profile={'이름':'김멋사'}
a=input("key값을 입력해주세요: ")
b=input("Value값을 입력해주세요: ")
profile[a]=b
print(profile)

#7
count=0
while 1:
    num=int(input("숫자를 입력해주세요: "))
    if(num==0):
        break
    if(num%2==0):
        count+=1
print("짝수의 개수는: ",count,"개")

