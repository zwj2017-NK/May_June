# May_June
python code\
人生苦短，我学python\
服务器配置定时任务的方法：\
1):sudo crontab -e\
  在打开的文本中写上自己的任务即可：\
   m h  dom mon dow   command\
   20 22 * * * /usr/bin/python2.7 /home/xxx/get_vt_report_mail.py >> /home/xxx/test.log\
  该任务的意思是在每天22:20的时候开始执行，并把程序的输出保存在test.log里面，注意：python程序里面所有的路径必须写成绝对路径，否则定时执行就会失败。\
  如果不知道Python的安装路径的话，用locate /bin/python2.7 搜索一下可以找到。\
  \
2)：sudo service cron restart\
  需要博客写的是重启cronb服务，但是对于Ubuntu系统来说没有cronb服务，而是要重启cron服务，可以用sudo service status命令查看当前服务的执行状态。如果服务没有开启，用sudo service cron start开启就行了。\
  \
3):sudo crontab -u root /var/spool/cron/crontabs/root\
  这一步是很关键的，具体作用暂不明确。\
