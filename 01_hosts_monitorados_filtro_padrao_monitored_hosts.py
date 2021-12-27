import json
from zabbix_api import ZabbixAPI
from zabbix_api import ZabbixAPIException
from zabbix_api import Already_Exists

URL = 'http://10.23.4.10'
USERNAME = 'Admin'
PASSWORD = 'zabbix'

try:
    zapi = ZabbixAPI(URL, timeout=180, validate_certs=False)
    zapi.login(USERNAME, PASSWORD)
    print(f'Conectado na API do Zabbix: {zapi.api_version()}')
except Exception as err:
    print(f'Falha para se conectar na API do Zabbix ({err}')
    exit(1)

host_mapping_status = {
    '0': 'habilitado',
    '1': 'desabilitado'
}

hosts = zapi.host.get({
    "output": ["host","name","status"],
    "monitored_hosts": 'qualquer coisa'
})
for host in hosts:
    host_name = host['host']
    host_visiblename = host['name']
    """
    host_status = host['status']
    if host_status == '0':
        host_status = 'habilitado'
    elif host_status == '1':
        host_status = 'desabilitado'
    """
    host_status = host_mapping_status.get(host['status'])
    print(f'{host_name};{host_visiblename};{host_status}')

