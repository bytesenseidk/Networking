class Network_Prefix(object):
    """ Calculates the netmask length """
    def __init__(self, subnet_mask="255.255.248.0"):
        self.subnet_mask = subnet_mask
        self.SNM = self.subnet_mask.split(".")
    

    def binary_string(self):
        """ Convert the dotted-decimal representation of the netmask to binary. """
        string = ""
        for octet in self.SNM:
            string += str("{0:08b}.".format(int(octet)))
        return string
    

    def netmask_len(self):
        """ Count number of contiguous 1 bits, starting with the most significant bit in the first octet (Left to Right) """
        binary_string = self.binary_string().split(".")
        prefix = 0
        for octets in binary_string:
            for bit in octets:
                prefix += int(bit)
        return prefix


    def __str__(self):
        return f"Prefix of subnet {self.subnet_mask} is /{self.netmask_len()}"


if __name__ == "__main__":
    prefix = Network_Prefix("255.255.255.0")
    print(prefix)