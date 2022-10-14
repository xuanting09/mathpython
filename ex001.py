''' 請撰寫一程式，輸入A組和B組各自的科目至集合中，以字串"end"作為結束（集合中不包含字串"end"。 請依序分行顯示 (1)A組和B組的所有科目 (2)A組和B組的共同科目 (3)B組有但A組沒有的科目 (4)A組和B組都沒有的科目
- **範例輸入**
    
    **Enter group A's subjects:** Math Literature English History Geography end
    
    **Enter group B's subjects:** Math Literature Chinese Physical Chemistry end
    
- **範例輸出**
    
    **['Chemistry', 'Chinese', 'English', 'Geography', 'History','Literature', 'Math', 'Physical'] 
    ['Literature', 'Math'] ['Chemistry', 'Chinese', 'Physical'] 
    ['Chemistry', 'Chinese', 'English', 'Geography', 'History', 'Physical']**
'''
ax=set()
b=set()
print("Enter group A's subjects:")
while True:
  en=input()
  if en=="end":
    
    break
  ax.add(en)

print("Enter group B's subjects:")
while True:
  e=input()
  if e=="end":
    
    break
  b.add(e)
 
 
 
# 印出下列四項 
# (1)A組和B組的所有科目
print(ax|b)
# (2)A組和B組的共同科目
print(ax&b)
# (3)B組有但A組沒有的科目
print(b-ax)
# (4)A組和B組都沒有的科目
print(ax-b)
