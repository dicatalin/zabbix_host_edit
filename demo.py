import json

import Python2ZabbixApi # class for manipulate zabbix hosts through api calls
import cred             # credentials and url file


host='dkr'              #zabbix hostname
hostg='apitestgroup2'        #zabbix group
inventory_section='site_notes' #inventory section to be updated
site_notes='site flooded'   #inventory info to be updated

zbxurl=cred.zbxurl
user=cred.user
password=cred.password


zbxi=Python2ZabbixApi.InitApi(zbxurl,user,password)

token=zbxi.GetToken()   #get token, when user pass authentication is used

resp=zbxi.GetHost(host,token)
hostid=resp["hostid"]

print(hostid)

# get groupid, will be used for host to group add
hostgroupid=zbxi.GetHostGroup(hostg, token)["groupid"]
print(hostgroupid)

# add inventory info
setinv=zbxi.SetInventory(hostid, inventory_section, site_notes, token)
print(setinv)

# add host to group
sethg=zbxi.SetHostGroup(hostid, hostgroupid, token)
print(sethg)
