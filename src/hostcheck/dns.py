# -*- coding: utf-8 -*-
from enum import Enum
from typing import Tuple

import dns.resolver


class DNSStatus(Enum):
    NOT_SET = "⚪"
    OK = "🟢"
    NOT_EXISTS = "🟡"
    NO_ANSWER = "🟠"


def is_resolved(host: str) -> Tuple[bool, DNSStatus]:
    result = True, DNSStatus.NOT_SET
    try:
        dns.resolver.resolve(host)
        result = True, DNSStatus.OK
    except dns.resolver.NXDOMAIN:
        result = False, DNSStatus.NOT_EXISTS
    except dns.resolver.NoAnswer:
        result = False, DNSStatus.NO_ANSWER
    return result
