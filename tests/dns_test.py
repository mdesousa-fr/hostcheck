# -*- coding: utf-8 -*-
import src.hostcheck.dns

VALID_HOST = "google.com"
NOT_EXISTS_HOST = "google.comz"
NO_ANSWER_HOST = "google"


class TestHostCheckDns:
    def test_dns_resolved(self):
        result = src.hostcheck.dns.is_resolved(VALID_HOST)
        assert result[0] and result[1] == src.hostcheck.dns.DNSStatus.OK

    def test_dns_not_exists(self):
        result = src.hostcheck.dns.is_resolved(NOT_EXISTS_HOST)
        assert not result[0] and result[1] == src.hostcheck.dns.DNSStatus.NOT_EXISTS

    def test_dns_no_answer(self):
        result = src.hostcheck.dns.is_resolved(NO_ANSWER_HOST)
        assert not result[0] and result[1] == src.hostcheck.dns.DNSStatus.NO_ANSWER
