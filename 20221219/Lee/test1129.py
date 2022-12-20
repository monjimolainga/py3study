#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:44:46 2022

@author: ryong
"""
'''
클래스에서 사용되는 연산자에 사용되는 특수 함수
+   __add__(self, other)
–	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
<	__lt__(self, other)
>	__gt__(self, other)
<=	__le__(self, other)
>=	__ge__(self, other)
==	__eq__(self, other)
!=	__ne__(self, other)

생성자 : __init__(self,...) : 클래스 객체 생성시 요구되는 매개변수에 맞도록 매개변수 구현
출력   : __repr__(self) : 클래스의 객체를 출력할때 문자열로 리턴.
'''
'''
   추상함수 : 자손클래스에서 강제로 오버라이딩 해야 하는 함수
             함수의 구현부에 raise NotImplementedError
             를 기술함
'''


'''
1. main이 실행 되도록  Rect 클래스 구현하기
    가로,세로를 멤버변수로.
    넓이(area),둘레(length)를 구하는 멤버 함수를 가진다
    클래스의 객체를 print 시 :  (가로,세로),넓이:xxx,둘레:xxx가 출력
[결과]
(10,20), 넓이:200,둘레:60
(10,10), 넓이:100,둘레:40
200 면적이 더 큰 사각형 입니다.
'''    
    
class Rect :
    width=0
    height=0
    def __init__(self,width,height) :
        self.width = width
        self.height = height
    def area(self) :    
        return self.width * self.height
    def length(self) :  
        return (self.width + self.height) * 2
    def __lt__(self,other):
        return self.area() < other.area()
    def __gt__(self,other):
        return self.area() > other.area()
    def __eq__(self,other):
        return self.area() == other.area()
    def __repr__(self):
        return("(%d,%d), 넓이:%d,둘레:%d" \
               % self.width,self.height,self.area(),self.length())

if __name__ == '__main__' :
    rect1=Rect(10,10)
    rect2=Rect(10,10)
    if rect1 > rect2 :
        print("%d 면적이 더 큰 사가형 입니다." % rect1.area())
    elif rect1 < rect2 :       
        print("%d 면적이 더 큰 사가형 입니다." % rect2.area())
    elif rect1 == rect2 :       
        print("면적이 같은 사가형 입니다.")

#코드는 맞는거 같은 결과값 print가 __repr__이 왜 출력이 안되는지 모르겠음
#소스는 코드문제들 중 Car클래스문제 참고해서 클래스 만들었고 
#main부분은 __name__='__main__'이라는게 생소해서 답안 참고했음




'''
2. main 이 실행 되도록, Calculator 클래스를 상속받은 
   UpgradeCalculator  클래스 구현하기
   
   Calculator  클래스
     value 멤버변수
     add 멤버함수 => 현재 value의 값에 매개변수로 받는 값을 더하기
   UpgradeCalculator 클래스
     minus 멤버함수 => 현재 value의 값에 매개변수로 받는 값을 빼기
'''   
 
class Calculator :
    value=0
    def add(self, other):
        self.value += other
        
class UpgradeCalculator(Calculator) :
    def minus(self, other):
        self.value -= other

main = UpgradeCalculator
main.add(5)
main.minus(4)
print(main.value)

#에러가 나는데 왜 나는지 모르겠음
#TypeError: add() missing 1 required positional argument: 'other'





'''
3. 2번에서 구현한 Calculator 클래스를 이용하여 
   MaxLimitCalculator 클래스 구현하기
MaxLimitCalculator 클래스에서 value 값은 절대 100 이상의 값을 가질수 없다.
'''
    
class MaxLimitCalculator(Calculator) :
     def value(self,v) :
        self.value += v
        if self.speed > 100 :
            self.speed = 99
        print("Max클래스value:%d" % self.speed)

mlc = MaxLimitCalculator()
mlc.value(200)

#+= 줄이 오류 unsupported operand type(s) for +=: 'method' and 'int'
#뭐가 문제인지 모르겠음 코드에 예시문제 car부분 참고한건데 type을 어떻게 고쳐야되는지 모르겠음





'''
4. 다음 코드는 알파벳 대문자의 모스 부호를 저장한 딕셔너리 데이터입니다. 
대문자 알파벳을 입력받아 알파벳의 해당하는 모스 부호를 출력하는 코드를 작성하시오 

[결과]
모스 부호로 표시할 단어(알파벳 대문자) : ABC
A : .-
B : -....
C : -.-.
'''
code = {'A':'.-', 'B':'-....', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.',
'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-',
'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..'}


sign = input("모스 부호로 표시할 단어(알파벳 대문자) : ")
for i in range(len(sign)) :
    print(sign[i],":",code[sign[i]])














'''
5. 학생들의 시험 성적가 다음과 같은 경우 성적의 합계와 평균을 출력하는 코드를 작성하시오
[결과]
총합: 355 ,평균: 71.0
'''
import re
data= 'hong:90,lee:80,kim:75,park:50,song:60'
c = data.split(",")
print(c)
numbers = re.sub(r'[^0-9]', '', c)
print(numbers)
#리스트에서 숫자만 뽑아내는 걸 해서 하려고했는데 에러가 납니다..
ssum=sum(numbers)
mean=ssum/len(numbers)
print("총합:%d ,평균:%d" % (ssum,mean))
#오류가 있어서 결과는 도출하지 못했음.









