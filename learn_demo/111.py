'''
1、输入一个年份，判断这个年份是不是闰年
规则：四年一润，百年不润，四百年又润
2、输入三角形三条边的长度，判断是否构成三角形
规则：任意两边长度和大于第三边的长度
'''

year = int(input("请输入年份："))
if year / 4 == 0 or year / 400 == 0:
    print('今年是闰年')
else:
    print("今年不是闰年")

a = int(input("请输入第一条边长a："))
b = int(input("请输入第一条边长b："))
c = int(input("请输入第一条边长c："))
if a + b > c or a + c > b or a + c > b:
    print('这是一个三角形')
else:
    print("this is not a 三角形")
