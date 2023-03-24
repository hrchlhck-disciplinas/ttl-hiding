import socket

from scapy.all import *

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketfd:
    socketfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socketfd.bind(('0.0.0.0', 8888))

    socketfd.listen()

    while True:
        print("Esperando conexões")

        conn, addr = socketfd.accept()

        print("Conexão estabelecida", addr)
        while True:
            data = conn.recv(512)
            
            if not data:
                break
            
            # Recebe pacote
            p = IP(data)
            msg = p[Raw].load.decode('utf8')

            # Envia pacote
            p_new = IP(dst=p.dst) / TCP(dport=p[TCP].dport) / Raw(load=msg.upper())
            conn.send(bytes(p_new))
