a=set()
b=set()
c= {"芒果", "草莓", "水梨", "芭樂", "楊桃", "番茄", "火龍果", "奇異果", "哈密瓜", "葡萄", "西瓜"} 
print("輸入小明水果店的水果:")
while True:
    enter=input()
    if enter=="結束":
        break
    a.add(enter) 

print("輸入大明水果店的水果:")
while True:
  enter=input()
  if enter=="結束":
    break
  b.add(enter)
print('小明水果店的水果')
print(a)
print('大明水果店的水果')
print(b)
print('全部有的水果')
print(c) 

print('小明水果店和大明水果店的所有水果')
print(a | b)                # 聯集

print('小明水果店和大明水果店的共同水果')
print(a & b)                # 交集

print('小明水果店沒有進的水果')
print(c - a)                # 差集

print('大明水果店沒有進的水果')
print(c - b)                # 差集

print('小明水果店跟大明水果店都沒有進的水果')
print(c - a - b ) 

print('大明水果店有但是小明水果店沒有的水果')
print(b - a)                # 差集
