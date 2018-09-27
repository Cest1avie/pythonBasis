dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

print("print-dict[a]:{0}".format(dict['a']))

del dict['e']
try:
    print("print-dict['e']:{0}".format(dict['e']))
except KeyError as e:
    print("字典中无此键{0}".format(e))
except Exception as e:
    print(e)

dict['f'] = 6 #新增键值对
print("print-dict['f']:{0}".format(dict['f']))

dict['a'] = 4   #修改原有键值对
print("print-dict['a']:{0}".format(dict['a']))

#dict.clear() 清空字典所有词条
#del dict 删除字典

print("字典元素个数：%d"%len(dict)) #len()返回字典元素个数
print(dict.get("g","none"))  #get 按键返回值，若键不存在返回默认值
print(dict.keys())  #返回所有键的列表

#遍历字典
for k,v in dict.items():
    print(k,"--->",v)

for z in dict.values(): #dict.values()返回字典的值  dict默认是字典的键
    print(z)



print( '2' in dict) #in dict 只找键 不找值