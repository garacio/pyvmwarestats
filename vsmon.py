#! /usr/bin/env python

from pysphere import *

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[31m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

s = VIServer()
s.connect("vshost", "user", "pass")

hosts = s.get_hosts()
pm = s.get_performance_manager() 
for host in hosts:
	print bcolors.RED + '[+] host: ', host, bcolors.ENDC
	counters = pm.get_entity_counters(VIMor(host, MORTypes.HostSystem))
	for c in counters:
		print bcolors.YELLOW + '    [-] ', c, ' ', counters[c], bcolors.ENDC
		print bcolors.GREEN + '        [--] ', pm.get_entity_statistic(host, counters[c]), bcolors.ENDC