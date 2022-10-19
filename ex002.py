a=input()
b=input()
bb = [int(b) for b in str(b)]
aa = [int(a) for a in str(a)]
a=0
if aa[1]==aa[3] or aa[1]!=aa[5] or bb[1]==bb[3] or bb[1]!=bb[5] :
    a=a+1
if aa[6]==1 or bb[6]==0:
    a=a+2
if aa[1]==bb[1] or aa[3]==bb[3] or aa[5]==bb[5] :
    a=a+3
if a==1:
    print('A')
if a==3:
    print('AB')
if a==4:
    print('AC')
if a==5:
    print('BC')
if a==6:
    print('ABC')
if a==0:
    print('None')

      