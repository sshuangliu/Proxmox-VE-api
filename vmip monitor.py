import threading
import time
import subprocess
from queue import Queue
from sql_orm_peewee import ip_monitor_db

WORD_THREAD = 50
IP_monitor_list = ip_monitor_db.select()
# print(IP_monitor_list)
IP_QUEUE = Queue()
for i in IP_monitor_list:
	IP_QUEUE.put(i.manage_ip)


def live_monitor():
	while not IP_QUEUE.empty():
		ip = IP_QUEUE.get()
		# if the ip is alive,res = 0,otherwise res = 1
		res = subprocess.call(f'ping -n 2 -w 5 {ip}', stdout = subprocess.PIPE)
		if not res:
			print(f'{ip }: {res} True')
			ip_monitor_item = ip_monitor_db.get(ip_monitor_db.manage_ip == ip)
			ip_monitor_item.online_or_not = True
			ip_monitor_item.sent_or_not = False
			ip_monitor_item.save()
		else:
			print(f'{ip }: {res} False')
			ip_monitor_item = ip_monitor_db.get(ip_monitor_db.manage_ip == ip)
			ip_monitor_item.online_or_not = False
			ip_monitor_item.save()



if __name__ == '__main__':
	threads = []
	start = time.perf_counter()
	for i in range(WORD_THREAD):
		thread = threading.Thread(target=live_monitor)
		thread.start()
		threads.append(thread)

	for thread in threads:
		thread.join()

	print()
	print("all done: time", time.perf_counter() - start, "\n")
    
