import requests
import urllib3
from requests.auth import HTTPBasicAuth

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def rest_session():
    url_rest = "https://192.168.0.101:8006/api2/json/access/ticket"
    data_rest = { "username":"root@pam","password":"GB2312"}
    client = requests.session()
    r = client.post(url=url_rest, json=data_rest, verify=False)
    print(r.json())

    return client  # 返回有状态话的会话

def get():
    client = rest_session()
    r = client.get(url="https://192.168.0.101:8006/api2/json/nodes", verify=False)
    print(r.request.headers)
    # print(r.json())


if __name__ == '__main__':
    # get()
    rest_session()