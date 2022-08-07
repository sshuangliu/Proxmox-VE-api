from asyncio.windows_events import NULL
import sqlite3
from datetime import datetime, timedelta


def create_tab():
    conn = sqlite3.connect('ip_monitor_db.sqlite3')
    c = conn.cursor()
    #  创建表
    sql = '''
        CREATE TABLE ip_monitor_db(
        ID INTEGER PRIMARY KEY  AUTOINCREMENT,
		manage_ip text NOT NULL UNIQUE,
        online_or_not bool NOT NULL,
		monitor_or_not bool NOT NULL,
        sent_or_not bool NOT NULL,
        last_sent_time datetime NOT NULL)
        '''
    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()


def insert_tab(manage_ip, online_or_not = True, monitor_or_not= True, last_sent_time = datetime.now(), sent_or_not = False):
    conn = sqlite3.connect('ip_monitor_db.sqlite3')
    c = conn.cursor()
    #  插入表
    sql = '''INSERT INTO ip_monitor_db(manage_ip, online_or_not, monitor_or_not, last_sent_time, sent_or_not) VALUES (?,?,?,?,?)'''
    c.execute(sql, (manage_ip, online_or_not, monitor_or_not, last_sent_time, sent_or_not))
    conn.commit()
    c.close()
    conn.close()

def update_tab(manage_ip, online_or_not=NULL, last_sent_time = NULL, sent_or_not = NULL):
    conn = sqlite3.connect('ip_monitor_db.sqlite3')
    c = conn.cursor()
    #  更新表
    sql = '''UPDATE ip_monitor_db SET online_or_not = ?, last_sent_time = ?, sent_or_not = ? WHERE manage_ip = ?'''
    c.execute(sql, (online_or_not, last_sent_time, sent_or_not, manage_ip))
    conn.commit()
    c.close()
    conn.close()

def select_tab(column='*'):
    conn = sqlite3.connect('ip_monitor_db.sqlite3')
    c = conn.cursor()
    #  查询表
    sql = f'''SELECT {column} FROM ip_monitor_db'''
    results = c.execute(sql)
    results_all = results.fetchall()
    return results_all
    conn.commit()
    c.close()
    conn.close()



if __name__ == '__main__':
    #create_tab()
    #insert_tab(manage_ip='baidu.com')
    #insert_tab(manage_ip='114.114.114.114')
    #insert_tab(manage_ip='100.64.0.1')
    print(select_tab('manage_ip'))
    print(select_tab('manage_ip'))

