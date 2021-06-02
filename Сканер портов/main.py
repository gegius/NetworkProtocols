import scaner

if __name__ == "__main__":
    host_ip = input("Введите хост ip ")
    port_diapason = input("Введите диапозон портов (Через пробел. "
                          "Включительно) ").split(' ')
    protocol = input("TCP/UDP сканировать? ")
    scaner.multi_check(host_ip, int(port_diapason[0]), int(port_diapason[1]),
                       protocol)
