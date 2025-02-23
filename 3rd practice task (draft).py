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
raw = input('Enter number:')
try:
      num = int(raw)
      print(num)
except:
      print(raw)