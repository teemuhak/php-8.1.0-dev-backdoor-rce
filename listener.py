#!/usr/bin/env python3
import argparse, sys, socket, io, time
from ipaddress import ip_address

def listen(args):
    p_to_int = int(args.p)
    buffer_size = 1024 * 128 # 128KB max message size, if don't understand this, leave it alone.

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((args.l, p_to_int))
    s.listen(1)
    print("Listening on", args.l + ":" + args.p, "...")

    conn, addr = s.accept()
    print("Connection recieved from", addr)

    while True:
        ans = conn.recv(buffer_size).decode()
        sys.stdout.write(ans)
        command = input()
        command += "\n"
        conn.send(command.encode())
        time.sleep(1)
        sys.stdout.write("\033[A" + ans.split("\n")[-1])
    
def main():

    parser = argparse.ArgumentParser(description="For when you're working from a machine lacking netcat.")
    parser.add_argument("-l", metavar=' -l <IP_ADDRESS> ', help="Set the listening host's IP address.")
    parser.add_argument("-p", metavar=' -p <PORT> ', help="Set the listening port.")
    
    args = parser.parse_args()

    listen(args)


if __name__ == "__main__":
    main()