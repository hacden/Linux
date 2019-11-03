#coding:utf-8   #强制使用utf-8编码格式
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
import sys

if len(sys.argv)<5 or len(sys.argv)>5 :
	print ("xxx.py sender@163.com  sender_password  to_user@163.com  msgtext")
else:
	my_sender=sys.argv[1] #发件人邮箱账号，为了后面易于维护，所以写成了变量
	my_pass=sys.argv[2]   #发件人邮箱的授权密码
	to_user=sys.argv[3] #收件人邮箱账号，为了后面易于维护，所以写成了变量
	msgtext=sys.argv[4]  #发送的内容
if len(sys.argv)==5:
	def mail(): 
		ret=True
		try:
			msg=MIMEText(msgtext,'plain','utf-8')
			msg['From']=formataddr(["hacden",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
			msg['To']=formataddr(["hacden",to_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
			msg['Subject']="服务器宕机情况通知" #邮件的主题，也可以说是标题

			server=smtplib.SMTP("smtp.163.com",25)  #发件人邮箱中的SMTP服务器，端口是25
			server.login(my_sender,my_pass)    #括号中对应的是发件人邮箱账号、邮箱密码
			server.sendmail(my_sender,[to_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
			server.quit()   #这句是关闭连接的意思
		except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
			ret=False
		return ret

	ret=mail()
	if ret:
		print("A mangaes sended ok!") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
	else:
		print("filed")  #如果发送失败则会返回filed