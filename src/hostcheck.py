# -*- coding: utf-8 -*-
import sys

import hostcheck.dns
from hostcheck.cmd import Args


def main():
    args = Args(sys.argv[1:])
    for h in args.hosts:
        dns = hostcheck.dns.DNSCheck(h)
        dns.resolve()
        print(
            f""">>> {h} <<<
        dns\t{dns.to_text()}"""
        )


if __name__ == "__main__":
    main()
