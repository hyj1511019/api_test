import os
# 数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '123456'
db = 'api_test'

# 路径配置
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(project_path,'data')
data_file = os.path.join(data_path,'data.xlsx')
log_file = os.path.join(project_path,'log','log.txt')
report_file = os.path.join(project_path,'report','report.html')

#邮件配置
smtp_server = 'smtp.163.com'
smtp_user = 'ivan-me@163.com'
smtp_password = 'hanzhichao123'

receiver = 'hyj1511019@163.com'
subject = '接口测试报告'
body = 'hi,all,\n附件中是接口测试报告，请查收'

is_send_report = True

# log配置
import  logging

logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file,
                    )




if  __name__ == "__main__":
    logging.info("hello, world")
    logging.info("中文日志")

