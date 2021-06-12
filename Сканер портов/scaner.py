import threading
from socket import *


def scan_tcp(ip, port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(0.1)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"\n{port}: TCP порт открытый")
        else:
            print(f"\n{port}: TCP порт закрытый")
    except:
        print(f"\n{port}: Ошибка подключения")
    finally:
        sock.close()


def scan_udp(ip, port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(0.1)
    try:
        sock.connect_ex((ip, port))
        try:
            sock.sendto(b'\x11', (ip, port))
        except:
            print(f"\n{port}: UDP порт закрытый")
        else:
            print(f"\n{port}: UDP порт открытый")
    finally:
        sock.close()


def multi_check(ip, start, finish, prot):
    global thread
    for port in range(start, finish + 1):
        if prot == "TCP":
            thread = threading.Thread(target=scan_tcp, args=(ip, int(port)))
        elif prot == "UDP":
            thread = threading.Thread(target=scan_udp, args=(ip, int(port)))
        thread.start()
