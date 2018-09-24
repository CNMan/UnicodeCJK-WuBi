from tkinter import *
import csv

常量_源数据文件 = "CJK-A.txt"
常量_修改后文件 = "修改" + 常量_源数据文件

# TODO: 如果Unicode编码为2xxxx, 图片在Plane02中
# 文件名格式统一为 U_xxxxxx.png （ xxxxxx 为 6 位 Unicode 编码，不足 6 位则前面补 0 ）
常量_图片路径_花园明朝 = "FontGlyphs/HanaMin/Plane00/U_"
常量_图片路径_汉仪仿宋 = "FontGlyphs/HYFangSong/Plane00/U_"
常量_图片路径_汉仪字典宋 = "FontGlyphs/HYZiDianSong/Plane00/U_"
常量_图片路径_细明体 = "FontGlyphs/MingLiU/Plane00/U_"
常量_图片路径_细明体_HKSCS = "FontGlyphs/MingLiU_HKSCS/Plane00/U_"
常量_图片路径_中易宋体 = "FontGlyphs/SimSun/Plane00/U_"
常量_图片路径_中华书局宋体 = "FontGlyphs/ZhongHuaSong/Plane00/U_"

常量_图片扩展名 = ".png"

常量_无 = "无"

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.创建控件()

    def 修改当前条目(self):
        self.当前字符[2] = self.编码86版值.get()
        self.当前字符[3] = self.编码98版值.get()
        # TODO: 置06版值
        print(str(self.字符列表))

    def 导出文件(self):
        with open(常量_修改后文件, 'w', newline='') as 目标文件:
            写文件 = csv.writer(目标文件, delimiter='\t')
            for 字符 in self.字符列表:
                写文件.writerow(字符)

    # TODO: 提示已到开头/末尾
    def 上一个字符(self):
        if (self.当前字符序号 > 0):
            self.当前字符序号 -= 1
        print("字符序号: " + str(self.当前字符序号))
        self.刷新控件()

    def 下一个字符(self):
        if (self.当前字符序号 < len(self.字符列表)):
          self.当前字符序号 += 1
        print("字符序号: " + str(self.当前字符序号))
        self.刷新控件()

    def 创建控件(self):
        self.当前字符序号 = 0
        self.字符列表 = []

        # 官方文档参考: https://docs.python.org/3/library/csv.html#module-contents
        with open(常量_源数据文件, newline='') as 源数据文件:
            源数据读取器 = csv.reader(源数据文件, delimiter='\t')
            for 行 in 源数据读取器:
                print(';'.join(行))
                self.字符列表.append(行)

        self.当前字符 = self.字符列表[self.当前字符序号]

        补0数 = 6 - len(self.当前字符[0])
        大写Unicode码 = "0" * 补0数 + self.当前字符[0].upper()

        图片区 = Frame(self)
        图片区.pack(side = "left")
        大陆字体区 = Frame(图片区)
        大陆字体区.pack()
        # TODO: 如图片不存在, 不应抛错
        # TODO: 重构
        # 显示图片, 参考: https://stackoverflow.com/questions/35024118/how-to-load-an-image-into-a-python-3-4-tkinter-window
        中易宋体图片 = PhotoImage(file=常量_图片路径_中易宋体 + 大写Unicode码 + 常量_图片扩展名)
        self.图片显示1 = Label(大陆字体区, image=中易宋体图片)
        self.图片显示1.image = 中易宋体图片
        self.图片显示1.pack(side = "left")

        中华书局宋体图片 = PhotoImage(file=常量_图片路径_中华书局宋体 + 大写Unicode码 + 常量_图片扩展名)
        self.图片显示2 = Label(大陆字体区, image=中华书局宋体图片)
        self.图片显示2.image = 中华书局宋体图片
        self.图片显示2.pack(side = "right")

        港台字体区 = Frame(图片区)
        港台字体区.pack()
        细明体_HKSCS图片 = PhotoImage(file=常量_图片路径_细明体_HKSCS + 大写Unicode码 + 常量_图片扩展名)
        self.图片显示3 = Label(港台字体区, image=细明体_HKSCS图片)
        self.图片显示3.image = 细明体_HKSCS图片
        self.图片显示3.pack(side = "left")

        细明体图片 = PhotoImage(file=常量_图片路径_细明体 + 大写Unicode码 + 常量_图片扩展名)
        self.图片显示4 = Label(港台字体区, image=细明体图片)
        self.图片显示4.image = 细明体图片
        self.图片显示4.pack(side = "right")

        日本字体区 = Frame(图片区)
        日本字体区.pack()
        花园明朝图片 = PhotoImage(file=常量_图片路径_花园明朝 + 大写Unicode码 + 常量_图片扩展名)
        self.图片显示5 = Label(日本字体区, image=花园明朝图片)
        self.图片显示5.image = 花园明朝图片
        self.图片显示5.pack()

        细节区 = Frame(self)
        细节区.pack(side = "right")
        # 显示文本, 参考https://www.python-course.eu/tkinter_labels.php
        self.Unicode编码区 = Frame(细节区)
        self.Unicode编码区.pack()
        self.Unicode编码显示提示 = Label(self.Unicode编码区, text = "Unicode编码")
        self.Unicode编码显示提示.pack( side = "left")
        self.Unicode编码值 = StringVar(value=self.当前字符[0])
        self.Unicode编码显示 = Label(self.Unicode编码区, textvariable=self.Unicode编码值)
        self.Unicode编码显示.pack(side = "right")

        self.笔顺区 = Frame(细节区)
        self.笔顺区.pack()
        self.笔顺提示 = Label(self.笔顺区, text = "笔顺")
        self.笔顺提示.pack( side = "left")
        # TODO: 读取实际数据
        self.笔顺值 = StringVar(value=常量_无)
        self.笔顺 = Label(self.笔顺区, textvariable=self.笔顺值)
        self.笔顺.pack(side = "right")

        修改区 = Frame(细节区)
        修改区.pack()
        可改编码区 = Frame(修改区)
        可改编码区.pack(side = "left")
        self.编码86版区 = Frame(可改编码区)
        self.编码86版区.pack()
        self.编码86版提示 = Label(self.编码86版区, text = "编码86版")
        self.编码86版提示.pack( side = "left")
        # 参考 https://stackoverflow.com/questions/20125967/how-to-set-default-text-for-a-tkinter-entry-widget
        self.编码86版值 = StringVar(value=self.当前字符[2])
        self.编码86版 = Entry(self.编码86版区, textvariable=self.编码86版值)
        self.编码86版.pack(side = "right")

        self.编码98版区 = Frame(可改编码区)
        self.编码98版区.pack()
        self.编码98版提示 = Label(self.编码98版区, text = "编码98版")
        self.编码98版提示.pack( side = "left")
        self.编码98版值 = StringVar(value=self.当前字符[3])
        self.编码98版 = Entry(self.编码98版区, textvariable=self.编码98版值)
        self.编码98版.pack(side = "right")

        self.编码06版区 = Frame(可改编码区)
        self.编码06版区.pack()
        self.编码06版提示 = Label(self.编码06版区, text = "编码06版")
        self.编码06版提示.pack( side = "left")
        self.编码06版值 = StringVar(value=常量_无)
        self.编码06版 = Entry(self.编码06版区, textvariable=self.编码06版值)
        self.编码06版.pack(side = "right")

        self.修改按钮 = Button(修改区, text = "修改", command = self.修改当前条目)
        self.修改按钮.pack(side = "right")

        self.遍历区 = Frame(细节区)
        self.遍历区.pack()
        self.上一个 = Button(self.遍历区, text = "上一个", command = self.上一个字符)
        self.上一个.pack( side = "left")

        self.下一个 = Button(self.遍历区, text = "下一个", command = self.下一个字符)
        self.下一个.pack(side = "right")

        # TODO: 搜索/浏览功能

        self.导出按钮 = Button(细节区, text = "导出文件", command = self.导出文件)
        self.导出按钮.pack()

    def 刷新控件(self):
        self.当前字符 = self.字符列表[self.当前字符序号]
        print("当前字符: " + str(self.当前字符))
        补0数 = 6 - len(self.当前字符[0])
        大写Unicode码 = "0" * 补0数 + self.当前字符[0].upper()
        
        中易宋体图片 = PhotoImage(file=常量_图片路径_中易宋体 + 大写Unicode码 + 常量_图片扩展名)
        self.图片显示1.configure(image=中易宋体图片)
        self.图片显示1.image = 中易宋体图片

        中华书局宋体图片 = PhotoImage(file=常量_图片路径_中华书局宋体 + 大写Unicode码 + 常量_图片扩展名)
        self.图片显示2.configure(image=中华书局宋体图片)
        self.图片显示2.image = 中华书局宋体图片

        细明体_HKSCS图片 = PhotoImage(file=常量_图片路径_细明体_HKSCS + 大写Unicode码 + 常量_图片扩展名)
        self.图片显示3.configure(image=细明体_HKSCS图片)
        self.图片显示3.image = 细明体_HKSCS图片

        细明体图片 = PhotoImage(file=常量_图片路径_细明体 + 大写Unicode码 + 常量_图片扩展名)
        self.图片显示4.configure(image=细明体图片)
        self.图片显示4.image = 细明体图片

        花园明朝图片 = PhotoImage(file=常量_图片路径_花园明朝 + 大写Unicode码 + 常量_图片扩展名)
        self.图片显示5.configure(image=花园明朝图片)
        self.图片显示5.image = 花园明朝图片

        self.Unicode编码值.set(self.当前字符[0])
        self.编码86版值.set(self.当前字符[2])
        self.编码98版值.set(self.当前字符[3])
        self.编码06版值.set(常量_无)
        self.笔顺值.set(常量_无)

root = Tk()
app = Application(master=root)
app.mainloop()