# -*- coding: utf-8 -*-
import sys

import hostcheck.dns
from hostcheck.cmd import Args


def main():
    args = Args(sys.argv[1:])
    print(args)
    for h in args.hosts:
        print(f"{h}: dns<{'🟢' if hostcheck.dns.is_resolved(h) else '🔴'}>")


if __name__ == "__main__":
    main()
