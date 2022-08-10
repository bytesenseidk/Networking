""" Subnet Table:
Subnet: |  1  |  2  |  4  |  8  | 16  |  32 |  64 | 128 | 256 |
Host:   | 256 | 128 |  64 |  32 | 16  |  8  |  4  |  2  |  1  |
SNM:    | /24 | /25 | /26 | /27 | /38 | /29 | /30 | /31 | /32 |
"""
class Subnet(object):
    def __init__(self, network_id, subnet_count):
        self.network_id = network_id.split("/")[0]
        self.subnet_count = subnet_count
        self.subnet_table = {
            "1": [256, 24], "2": [128, 25], "4": [64, 26], 
            "8": [32, 27], "16": [16, 28], "32": [8, 29], 
            "64": [4, 30], "128": [2, 31], "256": [1, 32]
        }
    
    # def __str__(self):
    #     specs = ["subnet", "host", "snm"]
    #     subnet_specs = self.subnet_specs(1)
    #     result = ''
    #     for index, spec in enumerate(specs):
    #         result += f"{spec}: {subnet_specs[index]}\n"
    #     return result
        
    def subnet_specs(self, subnet_count):
        while subnet_count < len(range(self.subnet_count)):
            return self.subnet_specs(subnet_count + subnet_count)
        data = self.subnet_table[str(subnet_count)]
        data.insert(0, subnet_count)
        return data
    
    def subnetworks(self):
        subnets_ids = []
        subnet_specs = self.subnet_specs(1)
        host_bit = int(self.network_id.split(".")[-1])
        for i in range(subnet_specs[0]):
            net_id = '.'.join(self.network_id.split(".")[:-1])
            subnets_ids.append(str(net_id + "." + str(host_bit)))
            host_bit += subnet_specs[1]
        return subnets_ids
        
        
if __name__ == "__main__":
    network_id = "192.168.4.0/24"
    subnets = 3
    temp = Subnet(network_id, subnets)
    print(temp.subnetworks())
    # print(temp)