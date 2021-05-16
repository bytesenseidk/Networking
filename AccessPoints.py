import os
import time
import pandas
from threading import Thread
from scapy.all import *

class AccessPointScanner(object):
    def __init__(self):
        self.networks = pandas.DataFrame(columns=["BSSID", "SSID", "dBm_signal", "Channel", "Crypto"])
        self.networks.set_index("BSSID", inplace=True)


    def callback(self, packet):
        if packet.haslayer(Dot11Beacon):
            bssid = packet[Dot11].addr2
            ssid = packet[Dot11Elt].info.decode()
            try:
                dbm_signal = packet.dBm_AntSignal
            except:
                dbm_signal = "N/A"
            stats = packet[Dot11Beacon].network_stats()
            channel = stats.get("channel")
            crupto = stats.get("crypto")
            self.networks.loc[bssid] = (ssid, dbm_signal, channel, crypto)
        
    
        

    def print_all(self):
        while True:
            os.system("clear")
            print(self.networks)
            time.sleep(.5)

if __name__ == "__main__":
    ap = AccessPointScanner()
    interface = "InterfaceName0mon"
    printer = Thread(target=ap.print_all)
    printer.daemon = True
    printer.start()
    sniff(prn=callback, iface=interface)