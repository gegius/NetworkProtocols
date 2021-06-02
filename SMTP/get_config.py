import configparser


def get_message_config(path):
    config = configparser.ConfigParser()
    config.read(path, encoding='utf-8')
    receivers = config.get('MESSAGE', 'receivers').split(',')
    topic = config.get('MESSAGE', 'topic')
    attachments = config.get('MESSAGE', 'attachments').split(',')
    if len(attachments) == 1 and attachments[0] == '':
        attachments = []
    return receivers, topic, attachments


def get_auth_info(path):
    config = configparser.ConfigParser()
    config.read(path)
    login = config.get('USER', 'login')
    password = config.get('USER', 'password')
    ip = config.get('USER', 'ip')
    return login, password, ip