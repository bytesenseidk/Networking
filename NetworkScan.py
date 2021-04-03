import psutil
from tabulate import tabulate

class Network_Details(object):
    def __init__(self):
        self.interfaces    = []
        self.address_ip    = []
        self.netmask_ip    = []
        self.broadcast_ip  = []
        self.address_mac   = []
        self.netmask_mac   = []
        self.broadcast_mac = []
        self.parser = psutil.net_if_addrs()
        self.scanner()

    def __repr__(self):
        data = {"Interface": [*self.active_interfaces()],
                "IP-Address": [*self.address_ip],
                "MAC-Address": [*self.address_mac],  
                "Netmask_IP": [*self.netmask_ip],
                "Netmask_MAC": [*self.netmask_mac],
                "Broadcast-IP": [*self.broadcast_ip],
                "Broadcast-MAC": [*self.broadcast_mac]
                }
        return tabulate(data, headers="keys", tablefmt="github")

    def active_interfaces(self):
        unique = []
        for interface in self.interfaces:
            if interface not in unique:
                unique.append(interface)
        return unique
    
    def scanner(self):
        for interface_name, interface_addresses in self.parser.items():
            for address in interface_addresses:
                self.interfaces.append(interface_name)
                if str(address.family) == 'AddressFamily.AF_INET':
                    self.address_ip.append(address.address)
                    self.netmask_ip.append(address.netmask)
                    self.broadcast_ip.append(address.broadcast)
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    self.address_mac.append(address.address)
                    self.netmask_mac.append(address.netmask)
                    self.broadcast_mac.append(address.broadcast)

if __name__ == "__main__":
    print(Network_Details())