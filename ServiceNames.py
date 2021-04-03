import socket

def find_service_name():
    ports = [80, 25]
    for port in ports: 
        print(f"Port: {port} >> Service Name: " 
              f"{socket.getservbyport(port, 'tcp')}")

        print(f"Port: {53} >> Service Name: "
              f"{socket.getservbyport(53, 'udp')}")

if __name__ == "__main__":
    find_service_name()
