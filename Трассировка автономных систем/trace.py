import os
import re
from get_date_from_ip import get_data


def trace(name):
    IP = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    cmd_line = f"tracert {name}"
    p = os.popen(cmd_line)
    stdout = p.read()
    return IP.findall(stdout)


def format_result(ips):
    with open("out.txt", "w") as f:
        f.write(
            "|  Number  |         IP         |         AS         |          Country          "
            "|     Provider               |\n")
        i = 0
        for item in ips:
            info = get_data(item)
            f.write("| " + str(i) + " " * (9 - len(str(i))) + "| " + str(
                item) + " " * (19 - len(item)) +
                    "| " + str(info[1]) + " " * (
                            19 - len(info[1])) + "| " + str(
                info[2]) + " " * (26 - len(info[2])) +
                    "| " + str(info[3]) + " " * (27 - len(info[3])) + "|\n")
            i += 1
