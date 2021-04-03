import socket
from tabulate import tabulate

class Ip_Host(object):
    def __init__(self, url="www.google.com"):
        self.url = url
        self.host_name = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.host_name)
        self.remote_ip = self.remote_info()
    
    def __repr__(self):
        data = {"Host Name:": [self.host_name],
                "IP-Address:": [self.ip_address],
                f"{self.url}:": [self.remote_ip]}
        table = tabulate(data, headers="keys", tablefmt="pretty")
        return table

    def remote_info(self):
        try:
            return socket.gethostbyname(self.url)
        except socket.error as err_msg:
            return err_msg

if __name__ == "__main__":
    print(Ip_Host())

