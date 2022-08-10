class Subnet(object):
    def __init__(self, network_id, subnets):
        self.network_id = network_id
        self.subnets = subnets

if __name__ == "__main__":
    network_id = "192.168.4.0/24"
    subnets = 3
    temp = Subnet(network_id, subnets)
    
    