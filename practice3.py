# ----------- 列表 ----------- #

# 访问列表元素
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

# pop() 删除元素，并能够继续使用它。根据元素序号。函数参数缺省时默认删除最后一个元素，类似栈的弹出
motorcycles=["honda","yamaha","suzuki"]
print(motorcycles)
popped_motorcycles=motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycles)

# remove() 删除元素，根据元素的值。注意：只删除第一个符合的元素
motorcycles=["honda","yamaha","suzuki"]
motorcycles.remove('honda') # 单引号也是可以的
print(motorcycles)

# 练习
guestList=["p0","p1","p2","p3"]
print(guestList)
unaviliable=1
print("Guest "+guestList[unaviliable]+" can't be here.")
del guestList[unaviliable]
guestList.insert(1,"pNew")
print(guestList)
print("We find a bigger table.")
guestList.insert(0,"pnew1")
guestList.insert(2,"pnew2")
guestList.append("pnew3")
print(guestList)
print("We can only have 2 guest.")

# sort()排序：永久性改变列表元素的排列顺序
cars=["bmw","audi","toyota","subaru"]
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# sorted()排序：临时排序，不改变原列表
cars=["bmw","audi","toyota","subaru"]
# cars[0]=cars[0].title()
print("Here is the list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the list again:")
print(cars)
print("Reverse sorted list:")
print(sorted(cars,reverse=True))

# reverse() 将列表倒序：永久改变列表，再reverse一遍即可改回来
cars=["bmw","audi","toyota","subaru"]
cars.reverse()
print(cars)

# len() 确定列表长度
print(len(cars))
















