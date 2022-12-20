#!/usr/bin/env python3
import sys
import socket


def get_accessible_ports(address, min_port, max_port):
	found_ports = []
	for port in range(min_port,max_port + 1):
		try:	
			s = socket.socket()
			s.settimeout(1)
			connect = s.connect_ex((address,port))
			if(connect == 0):
				found_ports.append(port)
				data = s.recv(1024)
				print(data)
			s.close()
		except Exception:
			pass
	# write code here
	return found_ports


def main(argv):
	address = sys.argv[1]
	min_port = int(sys.argv[2])
	max_port = int(sys.argv[3])
	ports = get_accessible_ports(address, min_port, max_port)
	for p in ports:
		print(p)

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 4:
		print('usage: python %s address min_port max_port' % sys.argv[0])
	else:
		main(sys.argv)
