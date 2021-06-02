import dnslib
from upd_rec import *


def update_cache_records(dns_answer, cache):
    for new_record in dns_answer.rr + dns_answer.ar + dns_answer.auth:
        record_type = new_record.rtype
        name = new_record.rname.label
        cache_records = cache[name]
        assert isinstance(dnslib.QTYPE.NS, object)
        assert isinstance(dnslib.QTYPE.A, object)
        assert isinstance(dnslib.QTYPE.AAAA, object)
        assert isinstance(dnslib.QTYPE.PTR, object)
        if record_type == dnslib.QTYPE.NS:
            update_ns(new_record, cache_records)
        elif record_type == dnslib.QTYPE.A:
            update_a(new_record, cache_records)
        elif record_type == dnslib.QTYPE.AAAA:
            update_aaaa(new_record, cache_records)
        elif record_type == dnslib.QTYPE.PTR:
            update_ptr(new_record, cache_records)
