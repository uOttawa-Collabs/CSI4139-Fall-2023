#!/usr/bin/env python3

import socket
import struct
import random

source_ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
source_port = random.randint(1, 65535)

target_ip = "172.17.0.2"
target_port = 161

# SMTP GetRequest
payload = b"\x30\x26\x02\x01\x01\x04\x06\x70\x75\x62\x6c\x69\x63\xa1\x19\x02" \
    b"\x04\x10\x10\x67\x3b\x02\x01\x00\x02\x01\x00\x30\x0b\x30\x09\x06" \
    b"\x05\x2b\x06\x01\x02\x01\x05\x00"


udp_header_length = 8
udp_header_dict = {
    "source_port": source_port,
    "destination_port": target_port,
    "length": udp_header_length + len(payload),
    "checksum": 0
}

ip_header_length = 20
ip_header_dict = {
    "version": 4,
    "ihl": 5,
    "tos": 0,
    "total_length": ip_header_length + udp_header_length + len(payload),
    "identification": 12345,
    "flags": 0,
    "fragment_offset": 0,
    "ttl": 64,
    "protocol": socket.IPPROTO_UDP,
    "header_checksum": 0,
    "source_address": socket.inet_aton(source_ip),
    "destination_address": socket.inet_aton(target_ip)
}


with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW) as raw_socket:
    ip_header = struct.pack(
        "!BBHHHBBH4s4s",
        ip_header_dict["version"] << 4 | ip_header_dict["ihl"],
        ip_header_dict["tos"],
        ip_header_dict["total_length"],
        ip_header_dict["identification"],
        ip_header_dict["flags"] << 13 | ip_header_dict["fragment_offset"],
        ip_header_dict["ttl"],
        ip_header_dict["protocol"],
        ip_header_dict["header_checksum"],
        ip_header_dict["source_address"],
        ip_header_dict["destination_address"]
    )

    udp_header = struct.pack(
        "!HHHH",
        udp_header_dict["source_port"],
        udp_header_dict["destination_port"],
        udp_header_dict["length"],
        udp_header_dict["checksum"]
    )

    udp_packet = ip_header + udp_header + payload
    raw_socket.sendto(udp_packet, (target_ip, target_port))

