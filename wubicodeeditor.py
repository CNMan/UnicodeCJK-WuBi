from tkinter import *
import csv

常量_源数据文件 = ["CJK-A.txt", "CJK-B.txt", "CJK-C.txt", "CJK-D.txt", "CJK-E.txt", "CJK-F.txt", "CJK.txt"]
# 暂时只指出导出到一个文件
常量_修改后文件 = "CJK-所有.txt"

常量_图片主目录 = "FontGlyphs/"
常量_图片路径 = {
  "中易宋体": "SimSun/",
  "中华书局宋体": "ZhongHuaSong/",
  "汉仪字典宋": "HYZiDianSong/",
  "汉仪仿宋": "HYFangSong/",
  "方正楷体S": "FZKaiS/",
  "细明体": "MingLiU/",
  "细明体_HKSCS": "MingLiU_HKSCS/",
  "方正楷体T": "FZKaiT/",
  "花园明朝": "HanaMin/",
}

常量_大陆字体列表 = ["中易宋体", "中华书局宋体", "汉仪字典宋", "汉仪仿宋", "方正楷体S"]
常量_台港澳字体列表 = ["细明体", "细明体_HKSCS", "方正楷体T"]
常量_日本字体列表 = ["花园明朝"]
常量_按地区名取字体列表 = {"中国大陆": 常量_大陆字体列表, "中国台港澳": 常量_台港澳字体列表, "日本": 常量_日本字体列表}

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
        print("已修改: " + str(self.当前字符))

    def 导出文件(self):
        with open(常量_修改后文件, 'w', newline='') as 目标文件:
            写文件 = csv.writer(目标文件, delimiter='\t')
            for 字符 in self.字符列表:
                写文件.writerow(字符)
        print("修改保存到: " + 常量_修改后文件)

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

    def 创建字体区(self, 区域, 地区名):
        字体区 = Frame(区域)
        字体区.pack()
        字体区提示 = Label(字体区, text = 地区名 + "字形")
        字体区提示.pack()
        字体显示 = Frame(字体区)
        字体显示.pack()
        for 字体 in 常量_按地区名取字体列表[地区名]:
            self.按字体取图片显示[字体] = self.创建图片显示(字体显示, 字体, "left")

    # TODO: 如图片不存在, 不应抛错
    # 显示图片, 参考: https://stackoverflow.com/questions/35024118/how-to-load-an-image-into-a-python-3-4-tkinter-window
    def 创建图片显示(self, 区域, 字体名, 位置):
        字体区 = Frame(区域)
        字体区.pack(side = 位置)
        字体提示 = Label(字体区, text = 字体名)
        字体提示.pack()
        try:
            图片 = PhotoImage(file=常量_图片主目录 + 常量_图片路径[字体名] + self.图片子路径)
        except:
            图片 = PhotoImage()
        图片显示 = Label(字体区, image=图片)
        图片显示.image = 图片
        图片显示.pack()
        return 图片显示

    def 创建五笔编码编辑区(self, 区域, 年份, 值):
        编码区 = Frame(区域)
        编码区.pack()
        编码提示 = Label(编码区, text = "编码" + 年份 + "版")
        编码提示.pack(side = "left")
        # 参考 https://stackoverflow.com/questions/20125967/how-to-set-default-text-for-a-tkinter-entry-widget
        编码值 = StringVar(value=值)
        编码 = Entry(编码区, textvariable=编码值)
        编码.pack(side = "right")
        return 编码值

    def 创建只读区(self, 区域, 提示文本, 值):
        # 显示文本, 参考https://www.python-course.eu/tkinter_labels.php
        区 = Frame(区域)
        区.pack()
        显示提示 = Label(区, text = 提示文本)
        显示提示.pack(side = "left")
        可变值 = StringVar(value=值)
        显示 = Label(区, textvariable=可变值)
        显示.pack(side = "right")
        return 可变值

    # Unicode编码->Plane号
    # 00xxxx 	Plane00
    # 01xxxx 	Plane01
    # 02xxxx 	Plane02
    # 03xxxx 	Plane03
    # 0Exxxx 	Plane14
    # 0Fxxxx 	Plane15
    # 10xxxx 	Plane16
    # 文件名格式统一为 U_xxxxxx.png （ xxxxxx 为 6 位 Unicode 编码，不足 6 位则前面补 0 ）
    def 组成图片子路径(self, Unicode码):
        Plane值 = "00"
        if (len(Unicode码) == 5):
            Plane值 = "0" + Unicode码[0]
        elif (len(Unicode码) == 6):
            前两位 = Unicode码[0:1]
            if 前两位 == '0E':
                Plane值 = "14"
            elif 前两位 == '0F':
                Plane值 = "15"
            elif 前两位 == '10':
                Plane值 = "16"
        补0数 = 6 - len(Unicode码)
        大写Unicode码 = "0" * 补0数 + Unicode码.upper()
        return "Plane" + Plane值 + "/U_" + 大写Unicode码 + 常量_图片扩展名

    def 读入源数据文件(self, 文件名):
        # 官方文档参考: https://docs.python.org/3/library/csv.html#module-contents
        with open(文件名, newline='') as 源数据文件:
            源数据读取器 = csv.reader(源数据文件, delimiter='\t')
            for 行 in 源数据读取器:
                self.字符列表.append(行)

    def 创建控件(self):
        self.当前字符序号 = 0
        self.字符列表 = []
        self.按字体取图片显示 = {}

        for 文件名 in 常量_源数据文件:
            self.读入源数据文件(文件名)

        self.当前字符 = self.字符列表[self.当前字符序号]
        self.图片子路径 = self.组成图片子路径(self.当前字符[0])

        图片区 = Frame(self)
        图片区.pack(side = "left")

        self.创建字体区(图片区, "中国大陆")
        self.创建字体区(图片区, "中国台港澳")
        self.创建字体区(图片区, "日本")

        细节区 = Frame(self)
        细节区.pack(side = "right")
        self.Unicode编码值 = self.创建只读区(细节区, "Unicode编码", self.当前字符[0])

        # TODO: 读取实际数据
        self.笔顺值 = self.创建只读区(细节区, "笔顺", 常量_无)

        修改区 = Frame(细节区)
        修改区.pack()
        可改编码区 = Frame(修改区)
        可改编码区.pack(side = "left")
        self.编码86版值 = self.创建五笔编码编辑区(可改编码区, "86", self.当前字符[2])
        self.编码98版值 = self.创建五笔编码编辑区(可改编码区, "98", self.当前字符[3])
        self.编码06版值 = self.创建五笔编码编辑区(可改编码区, "06", 常量_无)

        修改按钮 = Button(修改区, text = "修改", command = self.修改当前条目)
        修改按钮.pack(side = "right")

        遍历区 = Frame(细节区)
        遍历区.pack()
        上一个 = Button(遍历区, text = "上一个", command = self.上一个字符)
        上一个.pack(side = "left")

        下一个 = Button(遍历区, text = "下一个", command = self.下一个字符)
        下一个.pack(side = "right")

        搜索区 = Frame(细节区)
        搜索区.pack()
        self.搜索Unicode值 = StringVar(value="")
        Unicode值输入 = Entry(搜索区, textvariable=self.搜索Unicode值)
        Unicode值输入.pack(side = "left")

        搜索Unicode = Button(搜索区, text = "搜索Unicode", command = self.搜索Unicode)
        搜索Unicode.pack(side = "right")

        导出按钮 = Button(细节区, text = "导出文件", command = self.导出文件)
        导出按钮.pack()

    # 测试用: 3400 - A第一个, 20000 -B第一个
    # 支持大小写
    # TODO: 避免线性查找
    def 搜索Unicode(self):
        Unicode值输入 = self.搜索Unicode值.get().upper()
        字符序号 = -1
        已查到 = False
        for 字符 in self.字符列表:
            字符序号 += 1
            if (Unicode值输入 == 字符[0]):
                已查到 = True
                break
        if 已查到:
          self.当前字符序号 = 字符序号
          self.刷新控件()
        else:
          print("未找到Unicode码: " + Unicode值输入)

    def 刷新图片显示(self, 图片显示, 字体名):
        try:
            图片 = PhotoImage(file=常量_图片主目录 + 常量_图片路径[字体名] + self.图片子路径)
        except:
            图片 = PhotoImage()
        图片显示.configure(image=图片)
        图片显示.image = 图片

    def 刷新控件(self):
        self.当前字符 = self.字符列表[self.当前字符序号]
        print("当前字符: " + str(self.当前字符))
        self.图片子路径 = self.组成图片子路径(self.当前字符[0])
        
        for 字体 in 常量_图片路径.keys():
          self.刷新图片显示(self.按字体取图片显示[字体], 字体)

        self.Unicode编码值.set(self.当前字符[0])
        self.编码86版值.set(self.当前字符[2])
        self.编码98版值.set(self.当前字符[3])
        self.编码06版值.set(常量_无)
        self.笔顺值.set(常量_无)

root = Tk()
app = Application(master=root)
app.mainloop()