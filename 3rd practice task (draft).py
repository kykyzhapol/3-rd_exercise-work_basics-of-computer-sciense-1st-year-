#1st
price = input()
print(price[3])

#2nd
time = int(input())
print(f'{time//60**2} часов {int((time/60**2 - time//60**2)*60)} минут',
      f'{round((((time/60**2 - time//60**2)*60)-int((time/60**2 - time//60**2)*60))*60)} секунд')

#3rd
num = int(input())
print(num%(num//2))

import math

#4st
lst = list(map(int, input().split()))
print(f'{math.floor((lst[0]*100+lst[1])*lst[2]/100)} руб. {(lst[0]*100+lst[1])*lst[2]%100} коп.')
#5th
n = int(input())
print("(\___/) "*n, "(='.'=) "*n, '(")_(") '*n, sep='\n')

#6th
K = int(input())
N = int(input())
R = int(input())
print(str(K*R)*N)

#7th
raw = input('Enter number:')
try:
      num = int(raw)
      print(num)
except:
      print(raw)

#8th
import math
#cos(α) = (b2 + c2 - a2) / (2 * b * c)
A = int(input())
B = int(input())
C = int(input())
print(
      math.degrees(math.acos(((B**2)+(C**2)-(A**2))/(2*B*C))),
      math.degrees(math.acos(((A**2)+(C**2)-(B**2))/(2*A*C))),
      math.degrees(math.acos(((B**2)+(A**2)-(C**2))/(2*B*A)))
)

#9th
ATT = int(input())
COMP = int(input())
YDS = int(input())
TD = int(input())
INT = int(input())
a = ((COMP/ATT)-0.3)*5
b = ((YDS/ATT)-3)*0.25
c = (TD/ATT)*20
d = 2.375-(INT/ATT)*25
if a<0 or b<0 or c<0 or d<0:
    print(0)
else:
    print(((a+b+c+d)/6)*100)

#10th
num = list(map(int, input().split()))
print(int((num[0]/num[1]-num[0]//num[1])+(num[1]/num[0]-num[1]//num[0])+1))

#11th
clock = float(input())
print(int(clock//30), int((clock/30-clock//30)*60))

#12th
import time
print(time.ctime())

#13th
strb = int(input())
colb = int(input())
numb = int(input())
print(f'страница {numb//(strb*colb)+1} столбец {(numb%(strb*colb))//strb+1} строка {(numb-(strb*colb))%strb}')