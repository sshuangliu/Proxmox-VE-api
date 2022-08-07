from datetime import datetime, timedelta
import threading
import time
import zmail
from sql_orm_peewee import ip_monitor_db

class notice:

    def __init__(self):
        self.email_context = []

    # collecting all the devices which need to be further operation and save to self.email_context list
    def to_be_notice(self, db):
            if db.online_or_not == False and db.sent_or_not == False and db.monitor_or_not == True:
                db.sent_or_not = True
                db.last_sent_time = datetime.now()
                db.save()
                self.email_context.append({'manage_ip': db.manage_ip})
            if db.online_or_not == False and db.sent_or_not == True and db.monitor_or_not == True and (datetime.now() - timedelta(days=1))> db.last_sent_time:
                db.last_sent_time = datetime.now()
                db.save()
                self.email_context.append({'manage_ip': db.manage_ip})

    def my_send_mail(self):
        self.threading_tbn()
        if self.email_context:
            msg = 'Important notice:\n\n\nPlease check below devices\n'
            for i in self.email_context:
                msg = msg + 'manage_ip' + '\t' + i['manage_ip'] + '\n'
            print(msg)
            mail = {
                'subject': 'Important notice: MY Homelab Monitor alert',  # Anything you want.
                'content_text': msg # Anything you want.
                # 'attachments': ['/Users/zyh/Documents/example.zip','/root/1.jpg'],  # Absolute path will be better.
                }
            server = zmail.server('qwf22d6@qq.com', 'cigbf2ddewlqbdde')
            server.send_mail('xxxxxxx@163.com', mail)
            # server.send_mail(['foo@163.com','foo@126.com'],mail,cc=['bar@163.com'])

    # collecting all the necessary devices with multithread
    def threading_tbn(self):
        start = time.perf_counter()
        ip_monitor_base = ip_monitor_db.select()
        thread_list = [threading.Thread(target=self.to_be_notice, args=(item,)) for item in ip_monitor_base]
        for t in thread_list:
            t.start()
        for t in thread_list:
            if t.is_alive():
                t.join()

        #print(threading.active_count())
        print()
        print("all done: time", time.perf_counter() - start, "\n")


if __name__ == '__main__':
    my_notice = notice()
    my_notice.my_send_mail()
    # my_notice.threading_tbn()
