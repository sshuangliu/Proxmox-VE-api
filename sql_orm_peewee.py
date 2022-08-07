from peewee import *
import datetime


db = SqliteDatabase('ip_monitor_db.db')

class ip_monitor_db(Model):
    manage_ip = CharField(unique=True)
    online_or_not = BooleanField(default=True)
    monitor_or_not = BooleanField(default=True)
    sent_or_not = BooleanField(default=False)
    last_sent_time = DateTimeField(default=datetime.datetime.now)
    

    class Meta:
        database = db # if there are many databases ,This model uses the "testing.db" database.






if __name__ == '__main__':

    ############################# create DB and Tables
    # db.connect()
    # db.create_tables([ip_monitor_db,])
 
    ############################### insert items
    # ip1 = ip_monitor_db(manage_ip = 'baidu.com')
    # ip1.save()
    #ip2 = ip_monitor_db(manage_ip = '114.114.114.114', monitor_or_not = False)
    #ip2.save()
    # ip3 = ip_monitor_db.create(manage_ip = '100.64.0.1')

    ############################# query items
    # all = ip_monitor_db.select()
    # print(all)
    
    # all1 = ip_monitor_db.get(ip_monitor_db.manage_ip == 'baidu.com')
    # print(all1)
    # all2 = ip_monitor_db.select().where(ip_monitor_db.online_or_not == True)
    # all2 = ip_monitor_db.select().where(ip_monitor_db.online_or_not == True).get() # only get the first one element when there are many targets
    # print(all2)
    ##########################delete items
    # all3 = ip_monitor_db.delete().where(ip_monitor_db.monitor_or_not == False).execute()
    # print(all3)


    ####################################update items
    # all4 = ip_monitor_db.get(ip_monitor_db.manage_ip == 'baidu.com')
    # all4.manage_ip = '114.114.114.114'
    # all4.monitor_or_not = False
    # all4.save()
    # print(all4.manage_ip)
    # print(all4.monitor_or_not)

    ##############################reference
    # http://docs.peewee-orm.com/en/latest/peewee/query_examples.html
    # https://github.com/coleifer/peewee
    pass