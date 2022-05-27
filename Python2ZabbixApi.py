import requests
from requests.structures import CaseInsensitiveDict
import json

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json-rpc"


class InitApi:
    def __init__(self, target, user, passwd):
        self.target=target
        self.user=user
        self.passwd=passwd

    def GetToken(self):
        data = '{"jsonrpc": "2.0", "method": "user.login", "params": { "user": "'+self.user+'", "password": "'+self.passwd+'" }, "id": 1, "auth": null }'
        resp = requests.post(self.target, headers=headers, data=data)
        # parse response content:
        rsp = json.loads(resp.content)
        rsp=rsp["result"]
        # return token:
        return rsp
    def GetHost(self, host, token):
        data = '{"jsonrpc": "2.0", "method": "host.get", "params": { "filter": { "host": [ "'+host+'" ] } }, "auth": "'+token+'", "id": 1 }'
        resp = requests.post(self.target, headers=headers, data=data)
        resp = json.loads(resp.content)["result"][0]
        return resp
    def SetInventory(self, hostid, inventry, value, token):
        data = '{"jsonrpc":"2.0", "method":"host.update", "params":{ "hostid":"'+hostid+'", "inventory": { "'+inventry+'":"'+value+'" } }, "auth":"'+token+'", "id":1 }'
        resp = requests.post(self.target, headers=headers, data=data)
        return resp.content
    def GetHostGroup(self, hostgroup, token):
        data = '{"jsonrpc": "2.0", "method": "hostgroup.get", "params": { "output": ["name"], "filter": { "name": [ "'+hostgroup+'" ] } }, "auth": "'+token+'", "id": 1 }'
        resp = requests.post(self.target, headers=headers, data=data)
        rsp = json.loads(resp.content)
        rsp=rsp["result"][0]
        return rsp
    def SetHostGroup(self, hostid, hostgroupid, token):
        data = '{"jsonrpc": "2.0", "method": "hostgroup.massadd", "params": { "groups": { "groupid": "'+hostgroupid+'" }, "hosts": { "hostid": "'+hostid+'" } }, "auth": "'+token+'", "id": 1 }'
        resp = requests.post(self.target, headers=headers, data=data)
        return resp.content
