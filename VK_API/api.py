from urllib.request import urlopen
import json

access_token = '9eba420b9eba420b9eba420b149ec2554999eba9eba420bfe0df3b73cb2a579ed4420dc'
v = '5.74'


def make_request(method, fields):
    req = 'https://api.vk.com/method/{}?{}&v={}&access_token={}'.format(method,
                                                                        fields,
                                                                        '5.74',
                                                                        access_token)
    with urlopen(req) as url:
        j = json.loads(url.read())
    return j


def get_user(id_or_name):
    user = make_request('users.get', 'user_ids={}'.format(id_or_name))
    if user is not None and 'response' in user and 'error' not in user:
        return user


def get_user_friends(list_friends):
    for id in list_friends:
        if not is_deactivated(id):
            user_date = get_user(id)
            user_info = make_user_information(user_date)
            if user_date is not None and 'error' not in user_date and 'deactivated' not in user_date:
                user_friends = get_friends(id)
                if 'error' in user_friends:
                    friends_count = 'этот пользователь скрыл своих'
                else:
                    friends_count = str(user_friends['response']['count'])
                print("\nИмя/Фамилия пользователя: " + user_info +
                      '\n\nУ него/неё : ' + friends_count + " друзей" +
                      '\n\n id=' + str(id))
            else:
                print("Профиль друга закрыт для данного токена или удалён")


def get_user_information(user, field):
    if user is not None and 'response' in user:
        return user['response'][0][field]


def get_user_id(user):
    return get_user_information(user, 'id')


def is_deactivated(user_id):
    user = get_user(user_id)
    if user is not None:
        return 'deactivated' in user['response'][0].keys()


def get_friends(user_id, count=None):
    req_count = ''
    if count is not None:
        req_count = '&count={}'.format(count)
    return make_request('friends.get',
                        'user_id={}'.format(user_id) + req_count)


def get_friends_information(friends, field):
    return friends['response'][field]


def get_friends_list(friends):
    if 'error' in friends.keys():
        if friends['error']['error_code'] == 15:
            return 'private'
    return get_friends_information(friends, 'items')


def make_user_information(user):
    first_name = get_user_information(user, 'first_name')
    last_name = get_user_information(user, 'last_name')
    if first_name is None or last_name is None:
        return
    return last_name + ' ' + first_name


def get_albums(user_id):
    global access_token
    data = make_request("photos.getAlbums", 'user_id={}'.format(user_id))
    if 'error' in data:
        print('Этот профиль является приватным для данного токена')
        return
    print('\nКоличество альбомов: ' + str(data['response']['count']))
    for album in enumerate(data['response']['items']):
        print('\nНазвание: ' + str(
            album[1]['title']) + '\n' + 'Количество фото: ' + str(
            album[1]['size']))


if __name__ == '__main__':
    user_name_or_id = input("Введите id пользователя: ")
    user = get_user(user_name_or_id)
    id = get_user_id(user)
    if user is None:
        print("Пользователя не существует")
    else:
        req = input("Что вы хотите получить?\nВведите 'Друзья', "
                    "чтобы вывести список друзей пользователя,"
                    "\nВведите 'Альбомы',"
                    " чтобы вывести список альбомов пользователя: ")
        if req == 'Друзья':
            friends_count = input("Скольких друзей вы хотите увидеть? ")
            friends = get_friends(id, friends_count)
            friends_list = get_friends_list(friends)
            if friends_list == 'private':
                print('Этот профиль является приватным для данного токена')
            else:
                print("\nДрузья " + user_name_or_id)
                get_user_friends(friends_list)
        elif req == 'Альбомы':
            print("\nАльбомы " + user_name_or_id)
            print(get_albums(id))
        else:
            print('Некорректный запрос')
