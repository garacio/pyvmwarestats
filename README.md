pyvmwarestats
=============

Python vmware statistics

pip install -r requirements.txt

./vsmon.py -H srvaddr -U user -P password

NOTE:
To use Zabbix template host should have macros:
{$IPADDR} => real.vm.host.IP
