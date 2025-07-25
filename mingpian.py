import xlrd  #引入这个模块对Excel文件进行操作

execl = xlrd.open_workbook('') #打开Excel文件

sheet = execl.sheet_by_index(0)  #获取第一个工作表

names = []  #创建一个空列表来存储姓名
nicks = []  #创建一个空列表来存储昵称
works = []  #创建一个空列表来存储职位
for i in range(1, sheet.nrows):  #从第二行开始遍历
    