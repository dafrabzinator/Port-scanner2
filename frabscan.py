import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    ip='192.168.1.1'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(args.timeout)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port}: Open")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Port scanner')
    parser.add_argument('ip', help='Target IP address')
    parser.add_argument('--start-port', help='Starting port', default=1, type=int)
    parser.add_argument('--end-port', help='Ending port', default=1000, type=int)
    parser.add_argument('--timeout', help='Connection timeout', default=1, type=int)
    args = parser.parse_args()
    with ThreadPoolExecutor() as executor:
        for port in range(args.start_port, args.end_port+1):
            executor.submit(scan_port, args.ip, port)

