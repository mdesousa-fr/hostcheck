# -*- coding: utf-8 -*-
import argparse
from dataclasses import dataclass
from typing import List


@dataclass
class Args:
    hosts: List[str]
    dns: bool
    cert: bool

    def __init__(self, args: list) -> None:
        parser = argparse.ArgumentParser(description="Check your host web connectivity")
        parser.add_argument("host", type=str, nargs="+", help="Host to target")
        parser.add_argument(
            "-d, --dns", action="store_true", dest="dns", help="Check DNS informations"
        )
        parser.add_argument(
            "-c, --cert",
            action="store_true",
            dest="cert",
            help="Check certificate information",
        )
        parsed_args = parser.parse_args(args)
        self.hosts = parsed_args.host
        self.dns = parsed_args.dns
        self.cert = parsed_args.cert
