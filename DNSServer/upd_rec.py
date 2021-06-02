from dns_object import DNSObject


def update_ns(new_record, cached_records):
    if cached_records.ns is None:
        cached_records.ns = DNSObject(new_record.ttl)
    cached_records.ns.objects.append(new_record.rdata.label.label)


def update_a(new_record, cached_records):
    if cached_records.a is None:
        cached_records.a = DNSObject(new_record.ttl)
    cached_records.a.objects.append(new_record.rdata.data)


def update_aaaa(new_record, cached_records):
    if cached_records.aaaa is None:
        cached_records.aaaa = DNSObject(new_record.ttl)
    cached_records.aaaa.objects.append(new_record.rdata.data)


def update_ptr(new_record, cached_records):
    if cached_records.ptr is None:
        cached_records.ptr = DNSObject(new_record.ttl,
                                       new_record.rdata.label.label)
