import gzip
from colorama import Fore
import ipaddress
import datetime
import math
import sys

PROT_NAMES = {
    1: 'ICMP',
    2: 'IGMP',
    4: 'IPv4',
    6: 'TCP ',
    17: 'UDP ',
    41: 'IPv6'}

FLAG_DICT = {
    'FIN': 1,
    'SYN': 2,
    'RST': 4,
    'PSH': 8,
    'ACK': 16,
    'URG': 32}


def parse_tcp_flags(flags_value):
    if flags_value is None:
        return None
    try:
        flags_list = []
        for flag_name in FLAG_DICT.keys():
            if FLAG_DICT[flag_name] & int(flags_value) != 0:
                flags_list.append(flag_name)
        return '+'.join(flags_list)
    except ValueError:
        return flags_value


def parse_protocol(p):
    try:
        return PROT_NAMES.get(int(p), p)
    except ValueError:
        return p


def date_string(epoch):
    try:
        enum = int(epoch)
        return datetime.datetime.fromtimestamp(enum).strftime('%H:%M:%S')
    except (ValueError, TypeError):
        return None


def print_ip(addr, ip):
    padding = abs(21 - len(addr))
    try:
        if ipaddress.ip_address(ip).is_global:
            print(Fore.WHITE, addr, end=' ' * padding)
        else:
            print(Fore.BLUE, addr, end=' ' * padding)
    except ValueError:
        print(Fore.BLUE, addr, end='')


def pprint_flowlog_line(d: dict):
    protocol = parse_protocol(d.get('protocol', None))
    tcpflags = parse_tcp_flags(d.get('tcp-flags', None))
    netw = f"{d.get('interface-id', '-')[0:8]}:{d.get('vpc-id', '-')[0:8]}:" \
           f"{d.get('subnet-id', '-')[3:11]}:{d.get('instance-id', '-')[0:6]}"
    srcaddr = f"{d.get('srcaddr', '-')}:{d.get('srcport', '-')}"
    dstaddr = f"{d.get('dstaddr', '-')}:{d.get('dstport', '-')}"
    srcip, dstip = d.get('srcaddr', '-'), d.get('dstaddr', '-')
    action = f"{d.get('action', '-')}"

    print(Fore.LIGHTBLACK_EX, netw, end='')
    print_ip(srcaddr, srcip)
    print(Fore.CYAN, "->", end=' ')
    print_ip(dstaddr, dstip)
    print(Fore.WHITE, size_string(d.get('bytes', 0)), end='')

    if action == 'ACCEPT':
        print(Fore.GREEN, action, end=' ')
    elif action == 'REJECT':
        print(Fore.RED, action, end=' ')

    print(d.get('log-status', '?'), end='')
    ds, de = date_string(d.get('start')), date_string(d.get('end'))

    if de is not None and ds is not None:
        print(Fore.LIGHTBLACK_EX, ds + '-' + de, end='')
    if protocol:
        print(Fore.WHITE, protocol, end='')
    if tcpflags:
        print(Fore.WHITE, tcpflags, end='')
    print("")


def size_string(b: int):
    try:
        b = int(b)
        u = {3: 'G', 2: 'Mb', 1: 'Kb', 0: 'b'}
        rf = int(math.log(b, 1024))
        r = b / (math.pow(1024, rf))
        if rf != 0:
            s = f"{r:.1f}" + f"{u[rf]}"
        else:
            s = f"{int(r)}" + f"{u[rf]}"
        return f"{s:<7}"
    except ValueError:
        return "-"


def pprint_flowlog(filename: str):
    try:
        with gzip.open(filename, 'rt') as f:
            schema = f.readline().strip().split(' ')
            for line in f.readlines():
                vals = line.strip().split(' ')
                line_dict = dict(zip(schema, vals))
                pprint_flowlog_line(line_dict)
    except BrokenPipeError:
        print("Abort")
        sys.stderr.close()
