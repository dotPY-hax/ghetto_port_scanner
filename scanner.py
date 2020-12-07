import socket
import sys

ips = [""]


def single_scan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    exit_code = s.connect_ex((ip, port))
    s.close()
    return exit_code == 0


def print_open_ports(open_ports):
    for port in open_ports:
        print("port {} open".format(port))


def sir_scan_a_lot(ips):
    for ip in ips:
        scan_ip(ip)


def scan_ip(ip):
    print("start scanning {}".format(ip))
    open_ports = []
    for port in range(1, 65535):
        result = single_scan(ip, port)
        if result:
            open_ports.append(port)
            print("port {} open".format(port))

    print("=" * 15 + "DONE" + "=" * 15)
    print_open_ports(open_ports)
    print("sänk ju for trävelling wis paiton")


def start():
    if len(sys.argv) != 2:
        print("usage: {} ip".format(sys.argv[0]))
    else:
        ip = sys.argv[1]
        scan_ip(ip)

start()
