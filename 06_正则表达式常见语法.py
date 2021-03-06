import re

rs = re.findall('\d','123')
rs = re.findall('\d*','456')
rs = re.findall('\d+','789')
rs = re.findall('a+','aaabcd')

print(rs)

# 分组的使用
rs = re.findall('\d{1,2}','chuan13zhi2')
rs = re.findall('aaa(\d+)b','aaa19b')
print(rs)

# 一般的正则表达式匹配一个\需要四个\
rs = re.findall('a\\\\bc','a\\bc')
print(rs)
print('a\\bc')

# 使用r原串
rs = re.findall(r'a\\rbc','a\\rbc')
print(rs)
