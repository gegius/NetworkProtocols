import threading
from dns_server import *
from io_cache import *
LOCK = threading.Lock()


def check_exit():
    global DNS_server
    while not DNS_server.is_exit:
        inp = input()
        if inp == 'exit':
            DNS_server.is_exit = True


if __name__ == '__main__':
    cache = unload_cache()
    host = input("Укажите ip-адрес хоста ")
    remote = input("Укажите ip-ДНС сервера ")
    DNS_server = DNSServer(cache)
    threading.Thread(target=check_exit).start()
    try:
        DNS_server.start(host, 53, remote)
    except OSError as e:
        print(f'{host}/{53} Уже занят')
    load_cache(cache)
