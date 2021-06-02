import pickle
from collections import defaultdict
from сache import Cache


def load_cache(cache):
    try:
        with open('cache.file', 'wb') as file:
            file.write(pickle.dumps(cache))
    except Exception as e:
        print(e)


def unload_cache():
    cache = defaultdict(Cache)
    try:
        with open('cache.file', 'rb') as file:
            old_cache = pickle.loads(file.read())
            cache = old_cache
            print("КЭШ загружен")
    except Exception as e:
        print("КЭШ пуст")
        return cache
