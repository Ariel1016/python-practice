#0
a=input("당신의 이름은?")
print("안녕,",a,"!")

#1
num=input("num을 입력하세요 : ")
print("num은 ",len(num),"자리 수입니다.")

#4
a=int(input("첫번째 정수를 입력하세요: "))
b=int(input("두번째 정수를 입력하세요: "))
c=int(input("세번째 정수를 입력하세요: "))
min=a
if(a<b):
    if(c<a):
        min=c
    else:
        min=a
elif(a>b):
    if(b>c):
        min=c
    else:
        min=b
print("가장 작은 수는",min,"이다")

#5
pi=3.14
r=int(input("반지름을 입려하세요: "))
Area=r*r*pi
if(r<0):
    print("잘못된 입력값입니다.")
else:
    if(Area>200):
        print("너무 큰 원의 넓이는 구하기가 힘들어요.")
    else:
        print("원의 넓이는",Area, "입니다.")

#6
a=int(input("정수를 입력하세요: "))
sum=0
for i in range(a+1):
    if(i%3==0):
        sum+=i
print("0부터",a,"까지 3의 배수의 합은",sum,"입니다.")
    
