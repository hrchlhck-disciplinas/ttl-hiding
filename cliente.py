import socket

from scapy.all import *

sv_addr = os.environ.get('SERVER_ADDR')
sv_port = int(os.environ.get('SERVER_PORT'))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketfd:
    socketfd.connect((sv_addr, sv_port))
    while True:
        data = input(">>> ")

        # Constroi pacote
        p = IP(dst=sv_addr) / TCP(dport=sv_port) / Raw(load=data)
        socketfd.send(bytes(p))

        # Recebe pacote
        p = IP(socketfd.recv(512))
        print('Recebido:', p[Raw].load.decode())
            