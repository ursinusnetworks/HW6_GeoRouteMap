import socket
import struct
import time

ICMP_ECHO_REQUEST = 8
ICMP_ECHO_REPLY = 0
ICMP_TTL_EXCEEDED = 11

def get_checksum(bs):
    """
    Compute the internet checksum for some bytes

    Parameters
    ----------
    bs: list of bytes
        Bytes on which to compute the checksum
    
    Returns
    -------
    Checksum
    """
    if len(bs) % 2 == 1:
        bs += bytes([0])
    shorts = struct.unpack("!" + "H"*(len(bs)//2), bs)
    c = 0
    for s in shorts:
        c = c + s
        if ( (c >> 16) & 0xffff) > 0:
            c = (c & 0xffff) + 1
    c = (~c) & 0xffff
    return c

def ping(ip, id, seq, payload, ttl=64, timeout=5):
    """
    Parameters
    ----------
    ip: string
        IP to ping
    id: int
        ID to use
    seq: int
        Sequence number to use
    payload: bytes
        payload to send
    ttl: int
        ttl to use in IP header
    timeout: float
        Timeout to use on socket
    
    Returns
    -------
    return dict(
        typ: int
            Type of message returned,
        code: int
            Code of message
        cksum: int
            Checksum
        id: int
            ID of return message
        seq: int
            Sequence number of returned message
        payload: bytes
            Payload of returned message
        dt: float
            Time, in milliseconds, elapsed between request and reply
        )
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sock.settimeout(timeout)
    sock.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
    ## TODO: Fill this in

def traceroute(ip, timeout=5):
    """
    Call ping in a loop, incrementing ttl until the echo reply
    is received.  Keep track of the IPs seen along the way

    Parameters
    ----------
    ip: string
        Destination IP to which to trace
    timeout: float
        Socket timeout to use
    
    Returns
    -------
    list of strings/None
        Each element is IP if the server returned an ICMP error/success,
        or None if it timed out at that ttl
    """
    ips = []
    ## TODO: Fill this in
    return ips

def plot_ips(ips):
    """
    Plot locations of IPs on a map

    Parameters
    ----------
    ips: list of string/None
        IPs that were traced
    """
    from urllib import request
    import json
    import numpy as np

    base_url = "http://ip-api.com/json"

    ## TODO: Fill this in