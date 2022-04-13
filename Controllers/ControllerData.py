import os
import xlrd

class CaseFile(object):
    curPath = os.path.abspath("../Datas")
    Path = os.path.join(curPath, r"case.xlsx")

    def __init__(self):
        """
        xlrd 最新版目前删除了xlsx的文件读取支持 最好使用vsrion = 1.2.0
        """
        print(self.Path)
        self.file = xlrd.open_workbook(self.Path)
        self.sheets = self.file.sheet_names()
        self.sheet_dict = {}
        self.file_dict()

    def sheet_file(self, sht=1, case=0, h=0):
        """
        :param sht: 指定sheet页进行case的跑
        :param case: 指定case 要从哪里跑
        :param h: 指定跑到哪一条case
        :return:
        """
        if sht < 0:
            self.read_sheet(0, self.sheet_dict.get(self.sheets[-1]), 0, h)
        elif sht >= len(self.sheets):
            for i in range(0, len(self.sheets)):
                self.read_sheet(0, self.sheet_dict.get(self.sheets[i]), 0, h)
        else:
            self.read_sheet(case, self.sheet_dict.get(self.sheets[sht]), sht, h)

    def read_sheet(self, case=0, n=0, sht=0, h=0):
        """
        :param case: 0代表对当前sheet页全部运行
        :param n: n代表当前sheet总的行数
        :param sht: sht代表当前要运行的sheet
        :param h: h代表当前要运行的最大行数
        :return:
        """
        if h != 0 and h <= self.sheet_dict[self.sheets[sht]]:
            for i in range(case, h):
                result = self.file.sheet_by_name(self.sheets[sht]).row_values(i)
                print(result)
        else:
            if case == 0:
                for i in range(case+1, n):
                    result = self.file.sheet_by_name(self.sheets[sht]).row_values(i)
                    print(result)
            elif case != 0 and case < self.sheet_dict.get(self.sheets[sht]):
                for i in range(case, n):
                     result = self.file.sheet_by_name(self.sheets[sht]).row_values(i)
                     print(result)
            else:
                for i in range(case, n):
                     result = self.file.sheet_by_name(self.sheets[sht]).row_values(i)
                     print(result)

    def file_dict(self):
        """
        主要是为了最开始的时候就获得全部的sheet 并且知道每个sheet的rows
        :return:
        """
        for i in self.sheets:
            self.sheet_dict[i] = self.file.sheet_by_name(i).nrows



if __name__ == '__main__':
    Demo = CaseFile()
    Demo.sheet_file(3)