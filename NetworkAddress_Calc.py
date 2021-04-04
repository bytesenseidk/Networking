""" Network Address and Prefix Calculator """

def binary_string(address="128.42.5.4"):
    """ Convert the dotted-decimal representation of the address to binary. """
    address = address.split(".")
    string = ""
    for octet in address:
        string += str("{0:08b}.".format(int(octet)))
    last_dot = string[-1]
    return string.strip(last_dot)


def netmask_length(binary_snm):
    """ Count number of contiguous 1 bits, starting with the most significant bit in the first octet (Left to Right) """
    binary_snm = binary_snm.split(".")
    prefix = 0
    for octets in binary_snm:
        for bit in octets:
            prefix += int(bit)
    return prefix


def logical_and_convertion(ip="128.42.5.4", snm="155.255.248.0"):
    """ Align the bits in both addressess, and perform a logical AND on each pair of the respective bits. """
    binary_address = ""
    for index, bit in enumerate(ip):
        if bit == "1" and snm[index] == "1":
            binary_address += "1"
        elif bit == "." and snm[index] == ".":
            binary_address += "."
        else:
            binary_address += "0"
    return binary_address


def decimal_string(binary_address="10000000.00101010.00000000.00000000"):
    """ Converts the binary network address to a dotted decimal representation """
    decimal_network_address = ""
    binary_address_list = binary_address.split(".")
    for bit in binary_address_list:
        decimal_network_address += str(int(bit, 2)) + "."
    last_dot = decimal_network_address[-1]
    return decimal_network_address.strip(last_dot)

    
if __name__ == "__main__":
    decimal_ip  = "193.1.2.129"
    decimal_snm = "255.255.255.0"
    binary_ip   = binary_string(decimal_ip)
    binary_snm  = binary_string(decimal_snm)
    prefix      = netmask_length(binary_snm)
    binary_netaddress  = logical_and_convertion(binary_ip, binary_snm)
    decimal_netaddress = decimal_string(binary_netaddress)
    print(f"IP-Address:       {decimal_ip}\n"
          f"Subnet Mask:      {decimal_snm}\n"
          f"Network Address:  {decimal_netaddress} \{prefix}")

