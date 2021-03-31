import scaner


def main():
    host_ip = input("Введите хост ip ")
    port_diapason = input("Введите диапозон портов (Через пробел. "
                          "Включительно) ").split(' ')
    for port in range(int(port_diapason[0]), int(port_diapason[1]) + 1):
        print(scaner.scan_tcp(host_ip, port))


if __name__ == "__main__":
    main()
