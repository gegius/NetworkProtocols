import re
from urllib.request import urlopen
from site_parse import parse
import configparser


def get_data(ip):
    config = configparser.ConfigParser()
    config.read('configure.ini', encoding='utf-8')
    AS = re.compile(config.get('REGULAR', 'AS'))
    CO = re.compile(config.get('REGULAR', 'CO'))
    PR = re.compile(config.get('REGULAR', 'PR'))
    if ip.startswith('192.168.') or \
            ip.startswith('10.') or \
            (ip.startswith('172.')
             and 15 < int(ip.split('.')[1]) < 32):
        return ip, '', '', ''
    try:
        with urlopen(f"https://www.nic.ru/whois/?searchWord={ip}") as f:
            site = f.read().decode('utf-8')
            return ip, parse(site, AS), parse(site, CO), \
                   parse(site, PR)
    except Exception as ex:
        print(ex)
        return ip, '', '', ''
