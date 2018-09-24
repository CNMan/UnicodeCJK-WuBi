from tkinter import *
import csv

常量_源数据文件 = "CJK-A.txt"

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

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.创建控件()

    def 修改当前条目(self):
        self.当前字符[2] = self.编码86版值.get()
        print(str(self.字符列表))

    def 导出文件(self):
        with open('CJK-修改.csv', 'w', newline='') as 目标文件:
            写文件 = csv.writer(目标文件, delimiter='\t')
            for 字符 in self.字符列表:
                写文件.writerow(字符)
        
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

        # TODO: 如图片不存在, 不应抛错
        # TODO: 其他图片; 界面排版
        # TODO: 重构
        # 显示图片, 参考: https://stackoverflow.com/questions/35024118/how-to-load-an-image-into-a-python-3-4-tkinter-window
        中易宋体图片 = PhotoImage(file=常量_图片路径_中易宋体 + 大写Unicode码 + 常量_图片扩展名)
        self.图片显示1 = Label(self, image=中易宋体图片)
        self.图片显示1.image = 中易宋体图片
        self.图片显示1.pack()

        中易宋体图片 = PhotoImage(file=常量_图片路径_中易宋体 + 大写Unicode码 + 常量_图片扩展名)
        self.图片显示2 = Label(self, image=中易宋体图片)
        self.图片显示2.image = 中易宋体图片
        self.图片显示2.pack()

        细明体_HKSCS图片 = PhotoImage(file=常量_图片路径_细明体_HKSCS + 大写Unicode码 + 常量_图片扩展名)
        self.图片显示3 = Label(self, image=细明体_HKSCS图片)
        self.图片显示3.image = 细明体_HKSCS图片
        self.图片显示3.pack()

        细明体图片 = PhotoImage(file=常量_图片路径_细明体 + 大写Unicode码 + 常量_图片扩展名)
        self.图片显示4 = Label(self, image=细明体图片)
        self.图片显示4.image = 细明体图片
        self.图片显示4.pack()

        花园明朝图片 = PhotoImage(file=常量_图片路径_花园明朝 + 大写Unicode码 + 常量_图片扩展名)
        self.图片显示5 = Label(self, image=花园明朝图片)
        self.图片显示5.image = 花园明朝图片
        self.图片显示5.pack()

        # 显示文本, 参考https://www.python-course.eu/tkinter_labels.php
        self.Unicode编码区 = Frame(self)
        self.Unicode编码区.pack()
        self.Unicode编码显示提示 = Label(self.Unicode编码区, text = "Unicode编码")
        self.Unicode编码显示提示.pack( side = "left")
        self.Unicode编码显示 = Label(self.Unicode编码区, text=self.当前字符[0])
        self.Unicode编码显示.pack(side = "right")

        self.Unicode字符区 = Frame(self)
        self.Unicode字符区.pack()
        self.Unicode字符提示 = Label(self.Unicode字符区, text = "Unicode字符")
        self.Unicode字符提示.pack( side = "left")
        self.Unicode字符 = Label(self.Unicode字符区, text=self.当前字符[1])
        self.Unicode字符.pack(side = "right")

        self.编码86版区 = Frame(self)
        self.编码86版区.pack()
        self.编码86版提示 = Label(self.编码86版区, text = "编码86版")
        self.编码86版提示.pack( side = "left")
        # 参考 https://stackoverflow.com/questions/20125967/how-to-set-default-text-for-a-tkinter-entry-widget
        self.编码86版值 = StringVar(root, value=self.当前字符[2])
        self.编码86版 = Entry(self.编码86版区, textvariable=self.编码86版值)
        self.编码86版.pack(side = "right")

        self.修改按钮 = Button(self, text = "修改", command = self.修改当前条目)
        self.修改按钮.pack()

        self.导出按钮 = Button(self, text = "导出文件", command = self.导出文件)
        self.导出按钮.pack()
        
root = Tk()
app = Application(master=root)
app.mainloop()