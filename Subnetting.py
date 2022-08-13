from tabulate import tabulate

class Subnet(object):
    def __init__(self, network_id, subnet_count):
        self.network_id = network_id.split('/')[0]
        self.subnet_count = subnet_count
        self.subnet_table = {
            "1": [256, 24], "2": [128, 25], "4": [64, 64],
            "8": [32, 27], "16": [16, 28], "32": [8, 29],
            "64": [4, 30], "128": [2, 31], "256": [1, 32]
        }
        self.subnet_specs = self.__subnet_specs(1)
    
    def __str__(self):
        return str(tabulate(self.subnetworks(), headers="keys", tablefmt="github"))
    
    def __subnet_specs(self, subnet_count):
        while subnet_count < len(range(self.subnet_count)):
            return self.__subnet_specs(subnet_count + subnet_count)
        data = self.subnet_table[str(subnet_count)]
        data.insert(0, subnet_count)
        return data
    
    