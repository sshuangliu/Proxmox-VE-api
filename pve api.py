import requests


# self-sign CA warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Pve_api(object):

    def __init__(self, ip, username = None, password = None, port = '8006'):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
        self.ticket = None

    '''
    ####### ticket data structure
    {
    "data":{
    "ticket": "PVE:root@pam:62EF3DBE::UPduHl969t0bv/eVUs54Ez5z86epC86WvUi81kAgGbs/zw2aZbD7l2loroqOV58/u+iZFrCFRlEsvIKDYskSx0NWM4eW7081u4eMHquHPOnfwm1fblUnIClfs0tNjxwA7ZmFTVsNDgvEPFG5Uw98K8sYDvHLHixSHQEU8+MUyRubeYaJCTNSzNW2FhX+gVZU3xe7hUZSAO2wo0BI5Ciz2tK8WFtAoh7o4UyLR0nJb8qCf1XV6SWUxrq4NpwnmcqEUg7GIjS4ueZ874tjbvnLUdBF62aiKVdECZjAtbxv3ocqKUlw1jN/Gl6xDfSEpgwQiQCKjG2gMdPrNdu9Fp2Tow==",
    "cap":{"vms":{"VM.Clone": 1, "VM.Backup": 1, "VM.Config.Options": 1, "VM.Snapshot": 1,…},
    "CSRFPreventionToken": "62EF3DBE:/7meKBIZRMV6lpaQ9G9uylNI+/5qHYq3+gDj1Oie6Tw",
    "username": "root@pam"
    }
    }

    '''


    def get_ticket(self):
        path = '/api2/json/access/ticket'
        url = 'https://' + self.ip + ':' + self.port + path
        r = requests.post(url=url, json={"username": self.username, "password": self.password}, verify=False)
        self.ticket = r.json() # dict rather than string
        return r.json()

    def ticket_node_list(self):
        path = '/api2/json/nodes'
        url = 'https://' + self.ip + ':' + self.port + path
        headers = {'CSRFPreventionToken': self.ticket['data']['CSRFPreventionToken'], 'Cookie': 'PVEAuthCookie=' + self.ticket['data']['ticket']}
        r = requests.get(url=url, headers=headers, verify=False)
        return r.json()


    def ticket_vm_list(self, node):
        path = f'/api2/json/nodes/{node}/qemu'
        url = 'https://' + self.ip + ':' + self.port + path
        headers = {'CSRFPreventionToken': self.ticket['data']['CSRFPreventionToken'], 'Cookie': 'PVEAuthCookie=' + self.ticket['data']['ticket']}
        r = requests.get(url=url, headers=headers, verify=False)
        return r.json()

    def ticket_vm_current(self, node, vmid):
        path = f'/api2/json/nodes/{node}/qemu/{vmid}/status/current'
        url = 'https://' + self.ip + ':' + self.port + path
        headers = {'CSRFPreventionToken': self.ticket['data']['CSRFPreventionToken'], 'Cookie': 'PVEAuthCookie=' + self.ticket['data']['ticket']}
        r = requests.get(url=url, headers=headers, verify=False)
        return r.json()

    def ticket_vm_start(self, node, vmid):
        path = f'/api2/json/nodes/{node}/qemu/{vmid}/status/start'
        url = 'https://' + self.ip + ':' + self.port + path
        headers = {'CSRFPreventionToken': self.ticket['data']['CSRFPreventionToken'], 'Cookie': 'PVEAuthCookie=' + self.ticket['data']['ticket']}
        r = requests.post(url=url, headers=headers, verify=False)
        return r.json()

    def token_vm_stop(self, node, vmid, token):
        path = f'/api2/json/nodes/{node}/qemu/{vmid}/status/stop'
        url = 'https://' + self.ip + ':' + self.port + path
        headers = {'Authorization': 'PVEAPIToken=' + token} # Authorization : PVEAPIToken=root@pam!myid=1e1b7cbd-e7553141525564c-c324519041e0
        r = requests.post(url=url, headers=headers, verify=False)
        return r.json()


if __name__ == '__main__':
    op = Pve_api(ip='192.168.0.101', username='root@pam', password='xxxx')
    print(op.ticket)
    # it must run 'get_ticket()' first to get a new ticket when you do the 'op' down below
    # op.get_ticket()
    # print(op.ticket)
    # print('@'*10)
    # print(op.ticket_node_list())
    # print('@'*10)
    # print(op.ticket_vm_list('pve01'))
    # print('@'*10)
    # print(op.ticket_vm_current('pve01', '104'))
    # print('@'*10)
    # print(op.ticket_vm_start('pve01', '104'))
    # print('@'*10)
    # print(op.token_vm_stop('pve01', '104', 'root@pam!myid=1e1b7cbd-e755-4171-b32c-c324519041e0'))
