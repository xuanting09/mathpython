''''咖哩屋(Curry):下午 11:00

麵食館(Noodle):上午 2:00

滷味店(Braised dish):上午 3:00
麥當勞(McDonald's):24 小時不打烊'''


x=int(input())
t=int(input())
if x==10 or (x==11 and t==00):
    print('Curry')
elif x==1 or x==12 or (x==2 and t==00):
    print('Noodle')
elif x==2 or (x==3 and t==00):
    print('Braised dish')

else:
    print("McDonald's")