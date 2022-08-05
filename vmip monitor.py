import django
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# 让任何一个Py文件都能加载Django项目的models模块

from learn.models import CMDB_ASSET, IP_monitor
from ping3 import ping
import threading
import time

def live_monitor(manage_ip):
	if ping(manage_ip):
		print(f'{manage_ip }: {ping(manage_ip)}')
		ip_monitor_item = IP_monitor.objects.get(manage_ip=manage_ip)
		ip_monitor_item.online_or_not = True
		ip_monitor_item.sent_or_not = False
		ip_monitor_item.save()
	else:
		ip_monitor_item = IP_monitor.objects.get(manage_ip=manage_ip)
		ip_monitor_item.online_or_not = False
		ip_monitor_item.save()		


def tttt():
	start = time.perf_counter()
	ip_monitor_base = IP_monitor.objects.all()
	thread_list = [threading.Thread(target=live_monitor, args=(item.manage_ip,)) for item in ip_monitor_base]
	for t in thread_list:
		t.start()
	for t in thread_list:
		if t.is_alive():
			t.join()

	#print(threading.active_count())
	print()
	print("all done: time", time.perf_counter() - start, "\n")



if __name__ == '__main__':
	tttt()

