import base64
import socket
import ssl
from format import form
from get_config import get_auth_info

ignore = False


def send(sock: socket.socket, command):
    print(f'C: {command}')
    sock.send(command.encode('utf-8'))
    if not ignore:
        data = sock.recv(4096)
        print(f"S: {data.decode('ascii', errors='ignore')}")


def send_mail_to(receiver, plain_text, topic, attachments):
    global ignore
    receiver_server = 'smtp.yandex.ru'
    login, password, ip = get_auth_info('date/configure.ini')
    login_en = base64.standard_b64encode(login.encode()).decode('ascii')
    password_en = base64.standard_b64encode(password.encode()).decode('ascii')
    context = ssl.create_default_context()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((receiver_server, 465))
        with context.wrap_socket(sock, server_hostname=receiver_server) as cur_socket:
            send(cur_socket, f'HELO {ip}\r\n')
            send(cur_socket, 'AUTH LOGIN\r\n')
            send(cur_socket, login_en + '\r\n')
            send(cur_socket, password_en + '\r\n')
            send(cur_socket, f'MAIL FROM:<{login}>\r\n')
            send(cur_socket, f'RCPT TO:<{receiver}>\r\n')
            send(cur_socket, f'DATA\r\n')
            ignore = True
            send(cur_socket, f'From: Me <{login}>\r\n')
            send(cur_socket, f'To: You <{receiver}>\r\n')
            send(cur_socket, f'Subject: {topic}\r\n')
            mime = form(plain_text, attachments)
            send(cur_socket, mime)
            ignore = False
            send(cur_socket, '\r\n.\r\n')
            send(cur_socket, 'QUIT\r\n')
