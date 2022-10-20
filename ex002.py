

num = int(input())
set1=set()
while num!=-9999:
    set1.add(num)
    num = int(input())

print('Length:',len(set1))
print('Max:',max(set1))
print('Min:',min(set1))
print('Sum:',sum(set1))

