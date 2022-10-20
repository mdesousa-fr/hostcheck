# -*- coding: utf-8 -*-
from dataclasses import dataclass
from enum import Enum

import dns.resolver


class DNSStatus(Enum):
    NOT_SET = "⚪"
    OK = "🟢"
    NOT_EXISTS = "🟡"
    NO_ANSWER = "🟠"


@dataclass(init=False)
class DNSCheck:
    host: str
    ip: str
    status: DNSStatus

    def __init__(self, host) -> None:
        self.host = host
        self.ip = list()
        self.status = DNSStatus.NOT_SET

    def resolve(self) -> bool:
        result = True
        try:
            self.ip = dns.resolver.resolve(self.host)[0].to_text()
            self.status = DNSStatus.OK
            result = True
        except dns.resolver.NXDOMAIN:
            self.status = DNSStatus.NOT_EXISTS
            result = False
        except dns.resolver.NoAnswer:
            self.status = DNSStatus.NO_ANSWER
            result = False
        return result

    def to_text(self) -> str:
        output = f"{self.status.value} | status: {self.status.name}, ip: {self.ip}"
        return output
