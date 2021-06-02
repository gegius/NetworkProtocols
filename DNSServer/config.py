import dnslib


def get_required_info(cache_records, query):
    q_type = query.q.qtype
    if q_type == dnslib.QTYPE.A:
        return cache_records.a
    elif q_type == dnslib.QTYPE.AAAA:
        return cache_records.aaaa
    elif q_type == dnslib.QTYPE.NS:
        return cache_records.ns
    elif q_type == dnslib.QTYPE.PTR:
        return cache_records.ptr