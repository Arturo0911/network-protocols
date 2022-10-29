#!/usr/bin/python3


from time import sleep
import struct
import ipaddress
import socket
import os


# starting the way to decode the packages sent
# ip decoding routine
class IP:
    def __init__(self, buff=None) -> None:
        header = struct.unpack('<BBHHHBBH4s4s', buff)
        self.ver = header[0] >> 4
        self.ihl = header[0] & 0xF

        self.tos = header[1]
        self.len = header[2]
        self.id = header[3]
        self.offset = header[4]
        self.ttl = header[5]
        self.protocol_num = header[6]
        self.sum = header[7]
        self.src = header[8]
        self.dst = header[9]

        # human readable ip addresses
        self.src_address = ipaddress.ip_address(self.src)
        self.dst_address = ipaddress.ip_address(self.dst)

        # map protocol constants and their names
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}

        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except Exception as e:
            print(f"[x] {e} No protocol for {self.protocol_num}")
        self.protocol = self.protocol_map[self.protocol_num]


"""def main():
    # sniffer = None
    # sock_protocol = None
    if os.name == "nt":
        sock_protocol = socket.IPPROTO_IP
    else:
    sock_protocol = socket.IPPROTO_ICMP
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, sock_protocol)
    sniffer.bind(("127.0.0.1", 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    try:
        while True:
            # reading the package
            raw_buffer = sniffer.recvfrom(65535)[0]
            # creating an ip header
            ip_header = IP(raw_buffer[0:20])
            # printing the detected host and protocols
            print(f"[*] Protocol: {ip_header.protocol} {ip_header.src_address} -> {ip_header.dst_address} ")
        pass
    except Exception as e:
        print(str(e))
        exit(1)"""


def main():
    try:
        while True:
            # log.progress(f"{os.name
            if os.name == "nt":
                sock_protocol = socket.IPPROTO_IP
            else:
                sock_protocol = socket.IPPROTO_TCP
            sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, sock_protocol)

            # making a binding to a host and port
            sniffer.bind(("127.0.0.1", 0))

            # we're going to make possible the connection
            # including the ip in the header of the capture
            sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

            if os.name == "nt":
                sniffer.ioctl(socket.SIO_RCVALL, socket.SIO_RCVALL)

            raw_buffer = sniffer.recvfrom(65535)[0]
            ip_header = IP(raw_buffer[0:20])
            print('Protocol: %s %s -> %s' % (ip_header.protocol,
                                             ip_header.src_address,
                                             ip_header.dst_address))
            sleep(1)

    except Exception as e:
        print(str(e))
        exit(1)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()
