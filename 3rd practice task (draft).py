
#1st
price = input()
print(price[3])

#2nd
time = int(input())
print(f'{time//60**2} часов {int((time/60**2 - time//60**2)*60)} минут',
      f'{round((((time/60**2 - time//60**2)*60)-int((time/60**2 - time//60**2)*60))*60)} секунд')
