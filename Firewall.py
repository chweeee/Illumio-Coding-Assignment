from ipaddress import ip_address

class Firewall:
	def __init__(self, path_name):

		#dictionary of tables for each of the 4 cases
		# key: IP address, value: port numbers
		self.tables = {}
		self.tables['inbound_tcp'] = {}
		self.tables['inbound_udp'] = {}
		self.tables['outbound_tcp'] = {}
		self.tables['outbound_udp'] = {}

		#Read file accodring to path name
		all_rules = open(path_name, "r", encoding='iso-8859-1')
		next(all_rules) #skip first row, just headers
		for row in all_rules:
			rule = row[0:len(row)-1] #removing newline
			rule = rule.split(",")
			self.populate_table(rule[0],rule[1],rule[2],rule[3])

	def populate_table(self, direction, protocol, port, ipAddr):
		table_name = direction + "_" + protocol
		table = self.tables[table_name]

		#case 1: port number + ip addr
		if('-' not in port and '-' not in ipAddr):
			try:
				table[ipAddr]
			except Exception:
				table[ipAddr] = []

			table[ipAddr].append(int(port))

		#case 2: port range + ip addr
		elif('-' in port and '-' not in ipAddr):
			port_list = self.convert_port_range(port)
			try:
				table[ipAddr]
			except Exception:
				table[ipAddr] = []

			for i in range(0, len(port_list)):
				table[ipAddr].append(port_list[i])

		#case 3: port number + ip range
		elif('-' not in port and '-' in ipAddr):
			ipaddr_list = self.convert_ip_range(ipAddr)
			for i in range(0, len(ipaddr_list)):
				try:
					table[ipaddr_list[i]]
				except Exception:
					table[ipaddr_list[i]] = []

				table[ipaddr_list[i]].append(int(port))

		#case 4: port range + ip range
		elif('-' in port and '-' in ipAddr):
			port_list = self.convert_port_range(port)
			ipaddr_list = self.convert_ip_range(ipAddr)
			for i in range(0, len(ipaddr_list)):
				try:
					table[ipaddr_list[i]]
				except Exception:
					table[ipaddr_list[i]] = []

				table[ipaddr_list[i]] += port_list

	def convert_port_range(self,port_range):
		#converts given range to actual numbers
		port_range = port_range.split('-')
		lower = int(port_range[0])
		upper = int(port_range[1]) + 1
		return list(range(lower, upper))

	def convert_ip_range(self,ip_range):
		#converts given range to actual numbers
		ip_range = ip_range.split('-')
		start_ip = int(ip_address(ip_range[0]).packed.hex(), 16)
		end_ip = int(ip_address(ip_range[1]).packed.hex(), 16) + 1
		ipaddr_list = []
		for ip in range(start_ip,end_ip):
			ipaddr_list.append(ip_address(ip).exploded)

		return ipaddr_list

	def print_all_tables(self):
		print("<<inbound_tcp>>")
		for k, v in self.tables['inbound_tcp'].items():
			print(k, v)

		print("\n<<inbound_udp>>")
		for k, v in self.tables['inbound_udp'].items():
			print(k, v)

		print("\n<<outbound_tcp>>")
		for k, v in self.tables['outbound_tcp'].items():
			print(k, v)

		print("\n<<outbound_udp>>")
		for k, v in self.tables['outbound_udp'].items():
			print(k, v)

	def accept_packet(self, direction, protocol, port, ipAddress):
		#returns true if matches rule, false if otherwise
		table_name = direction + "_" + protocol
		#decide which table to use base on table_name
		table = self.tables[table_name]

		if(ipAddress in table):
			ports = table[ipAddress]
			if(port in ports):
				return "true"
			else:
				return "false"
		else:
			return "false"
