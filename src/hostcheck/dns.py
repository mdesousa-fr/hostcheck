# -*- coding: utf-8 -*-
import dns.resolver


def is_resolved(host: str) -> bool:
    result = True
    try:
        dns.resolver.resolve(host)
    except dns.resolver.NXDOMAIN:
        result = False
    except dns.resolver.NoAnswer:
        result = False
    return result
