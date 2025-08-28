 import logging
 import re
 import socket
 import subprocess
 from ipaddress import IPv4Network
 
 		response = {}
 		response['status'] = False
 
		wafw00f_command = f'wafw00f {url}'
		output = subprocess.check_output(wafw00f_command, shell=True)
 		# use regex to get the waf
		regex = "behind \\\\x1b\[1;96m(.*)\\\\x1b"
		group = re.search(regex, str(output))

 		if group:
 			response['status'] = True
 			response['results'] = group.group(1)