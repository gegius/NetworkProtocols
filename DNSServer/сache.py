import time


def remain_ttl(obj):
    passed_time = int(time.time() - obj.init_time)
    return max(0, obj.ttl - passed_time)


class Cache:
    def __init__(self):
        self.a = None
        self.aaaa = None
        self.ns = None
        self.ptr = None

    def delete_expired_records(self):
        if self.a is not None and remain_ttl(self.a) == 0:
            self.a = None
        if self.aaaa is not None and remain_ttl(self.aaaa) == 0:
            self.aaaa = None
        if self.ns is not None and remain_ttl(self.ns) == 0:
            self.ns = None
        if self.ptr is not None and remain_ttl(self.ptr) == 0:
            self.ptr = None
