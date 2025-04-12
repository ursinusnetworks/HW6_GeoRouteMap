import argparse
import random
import time
import socket
from icmp import ping

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, required=True, help="Host to ping")
    parser.add_argument("--payload", type=str, default="Hello world this is CS 475 speaking!", help="ICMP message payload")
    parser.add_argument("--timeout", type=float, default=5, help="Timeout for each ping message, in seconds")
    parser.add_argument("--ttl", type=int, default=64, help="Time to live for each ping message")
    opt = parser.parse_args()
    host = opt.host
    payload = opt.payload.encode("ascii")
    timeout = opt.timeout
    ttl = opt.ttl

    (_, _, _, _, ip) = socket.getaddrinfo(host, 0, family=socket.AF_INET)[0]
    ip = ip[0]
    print("ip", ip)
    ## TODO: Fill this in