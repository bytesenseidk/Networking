"""
- The broadcast address converts all host bits to 1's.
- With 11 bits of the IP-address, we find the host mask by inverting the network address.
- Using the same addresses as above:
	- IP-address: 			128.42.5.4		In binary:	10000000.00101010.00000101.00000100
	- Host bit mask:		155.255.248.0	In binary:	00000000.00000000.00000hhh.hhhhhhhh
	- Force Host Bits:						_____________________________________________
	- Binary Broadcast:									10000000.00101010.00000111.11111111
	- Broadcast Address:	                            128     .42      .7       .255

"""
""" Broadcast Address Calculator """

def binary_string(address="128.42.5.4"):
    """ Convert the dotted-decimal representation of the address to binary. """
    address = address.split(".")
    string = ""
    for octet in address:
        string += str("{0:08b}.".format(int(octet)))
    last_dot = string[-1]
    return string.strip(last_dot)


def force_host_bits(ip="128.42.5.4", snm="155.255.248.0"):
    """ Align the bits in both addressess, and perform a force host bit operation on every host bit """
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
    decimal_snm = "155.255.248.0"
    binary_ip   = binary_string(decimal_ip)
    binary_snm  = binary_string(decimal_snm)
    binary_netaddress  = logical_and_convertion(binary_ip, binary_snm)
    decimal_netaddress = decimal_string(binary_netaddress)
    print(f"IP-Address:       {decimal_ip}\n"
          f"Subnet Mask:      {decimal_snm}\n"
          f"Network Address:  {decimal_netaddress}")
    print(binary_ip)
    print(binary_snm)
