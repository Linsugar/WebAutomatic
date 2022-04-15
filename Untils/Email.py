import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

from Controllers.ControllerConfig import ConfigParams


class SendEmail():
    sender: str
    receivers: str  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    curPath = os.path.abspath("../Datas")
    Path = os.path.join(curPath, r"case.xlsx")
    mail_host: str  # 设置服务器
    mail_user: str   # 用户名
    mail_pass: str   # 口令

    def __init__(self):
        # 创建一个带附件的实例
        self.message = MIMEMultipart()
        self.message['From'] = Header("迭代回归", 'utf-8')
        self.message['To'] = Header("测试", 'utf-8')
        self.subject = '关于本次邮件的迭代回归测试'
        self.message['Subject'] = Header(self.subject, 'utf-8')
        self.sender, self.receivers, self.mail_host, self.mail_user, self.mail_pass = ConfigParams().Email()


    def send_email(self):
        # 邮件正文内容
        self.message.attach(MIMEText('这是本次的测试结果反馈', 'plain', 'utf-8'))
        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open(self.Path, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="test.xlsx"'
        self.message.attach(att1)

        # 构造附件2，传送当前目录下的 runoob.txt 文件
        att2 = MIMEText(open(self.Path, 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename="runoob.xlsx"'
        self.message.attach(att2)

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, self. message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print(e)
            print("无法发送邮件")


if __name__ == '__main__':
    TestMail = SendEmail()
    TestMail.send_email()