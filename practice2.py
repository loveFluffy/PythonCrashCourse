# ========== 字符串的基本操作 ========== #

# 字符串大小写转换函数
infomessage="hello world"
print(infomessage.title())
print(infomessage.upper())
print(infomessage.lower())

# 用+合并字符串
firstName="Tom"
lastName="Riddle"
fullName=firstName+" "+lastName
print("\t"+fullName+"\nis happy!")

# 删除字符串末尾的空白
tmpStr=" Python Language "
print(tmpStr.rstrip()+".")
print(tmpStr+".")
# 这种删除并不会修改原变量
# tmpStr=tmpStr.rstrip()
# print(tmpStr+".")
# lstrip() strip()
print(tmpStr.lstrip()+".") # 删除开头的空白
print(tmpStr.strip()+".") # 删除两头的空白

# 双引号里可以使用单引号
print("Tom's cat.")
print('Tom"s cat')

# 加减乘除
print(1+2-3*4/5)
print(2**3) # 乘方

# 数字转字符串
age=23
print("Happy "+str(age)+"rd Birthday!")

# Python 之禅
import this
