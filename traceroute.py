import argparse
import socket
from icmp import traceroute, plot_ips

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, required=True, help="Host to ping")
    parser.add_argument("--timeout", type=float, default=5, help="Timeout for each ping message, in seconds")
    opt = parser.parse_args()
    host = opt.host
    timeout = opt.timeout

    (_, _, _, _, ip) = socket.getaddrinfo(host, 0, family=socket.AF_INET)[0]
    ip = ip[0]
    print("ip", ip)
    ips = traceroute(ip, timeout)
    print(ips)
    plot_ips(ips)