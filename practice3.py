# ----------- 列表 ----------- #

bicycles=["trek","cannondale","redline"]
print(bicycles) # 这种输出的是列表的内部表示
print(bicycles[0].title())
print(bicycles[-1].title()) # -1 访问最后一个元素
print("My first bicycle was a "+bicycles[0].title()+".")

# 修改列表元素
bicycles[0]="honda"
print(bicycles[0])

bicycles.append("ducati") # append()
print(bicycles[-1])
bicycles.insert(1,'tmp')
print(bicycles) # insert()

del bicycles[1]
print(bicycles)



















