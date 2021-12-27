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

subgroups = ['Linux', 'Windows']
name = 'Loja'

def create_new_hostgroup(group):
    try:
        create_hostgroup = zapi.hostgroup.create({
            "name": group
        })
        print(f'[{group}] - Hostgroup cadastrado com sucesso')
    except Already_Exists:
        print(f'[{group}] - O hostgroup ja existe')

for number in range(1,3):
    nome_loja = f'{name}{number:03d}'
    create_new_hostgroup(group=nome_loja)
    for subgroup in subgroups:
        nome_loja_subgroup = f'{nome_loja}/{subgroup}'
        create_new_hostgroup(group=nome_loja_subgroup)
