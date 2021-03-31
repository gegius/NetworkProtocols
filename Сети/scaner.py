import socket


def scan_tcp(ip, port: object) -> object:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            answer = f"\n{port}: TCP порт открытый"
        else:
            answer = f"\n{port}: TCP порт закрытый"
    except socket.error:
        answer = f"\n{port}: Ошибка подключения"
    finally:
        sock.close()
    return answer
