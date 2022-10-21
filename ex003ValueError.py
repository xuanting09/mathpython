try:
    x=int(input())  
    if x<=15:
        pl=input('parent license : ')
        if pl=='y':
            print('you can enter')
        elif pl=='n':
            print("you can't enter")
        else: 
            print("no this")
            
    elif x>15:
        ml=input('your license : ')
        if ml=='y':
            print('you can enter')
        elif ml=='n':
            print("you can't enter")
        else:
            print("no this")
   
except ValueError:
    print('型別發生錯誤')   

    