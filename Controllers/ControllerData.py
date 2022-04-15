import os
import xlrd
from Untils.LogFile import Logger
class CaseFile:
    curPath = os.path.abspath(r"../Datas")
    Path = os.path.join(curPath, r"case.xlsx")

    def __init__(self):
        """
        xlrd 最新版目前删除了xlsx的文件读取支持 最好使用vsrion = 1.2.0
        """
        self.log = Logger().logger
        print(self.Path)
        self.file = xlrd.open_workbook(r"D:\WebAutomatic\Datas\case.xlsx")
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

    def read_sheet(self, n=0, sht=0, h=0, dorun=0):
        """
        :param dorun:
        :param n: n代表当前sheet总的行数
        :param sht: sht代表当前要运行的sheet
        :param h: h代表当前要运行的最大行数
        :return:
        """
        if len(self.sheet_dict)-sht >= 0:
            shs = self.sheet_dict[self.sheets[sht]]
            case_list = []
            if n == 0 and sht == 0 and h == 0 and dorun == 0:
                """默认进行第一页的全部读取"""
                for i in range(1, shs):
                        result = self.file.sheet_by_name(self.sheets[sht]).row_values(i)
                        case_list.append(result)
                        print("case list == "+str(case_list))
            elif dorun != 0:
                """进行所有sheet页的用例数据读取"""
                for (k, v) in self.sheet_dict.items():
                    for i in range(1, v):
                        result = self.file.sheet_by_name(k).row_values(i)
                        case_list.append(result)
            else:
                """根据给的参数来执行对应sheet 的case"""
                if h < n >= 0:
                    for i in range(n+1, h):
                        result = self.file.sheet_by_name(self.sheets[sht]).row_values(i)
                        case_list.append(result)
                    print("case list1 == " + str(case_list))
                else:
                    for i in range(n+1, n+3):
                        result = self.file.sheet_by_name(self.sheets[sht]).row_values(i)
                        case_list.append(result)
                    print("case list2 == " + str(case_list))
            return case_list


    def file_dict(self):
        """
        主要是为了最开始的时候就获得全部的sheet 并且知道每个sheet的rows
        :return:
        """
        for i in self.sheets:
            self.sheet_dict[i] = self.file.sheet_by_name(i).nrows

if __name__ == '__main__':
    Demo = CaseFile()
    Demo.read_sheet(sht=2)