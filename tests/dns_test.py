# -*- coding: utf-8 -*-
import src.hostcheck.dns

VALID_HOST = "google.com"
NOT_EXISTS_HOST = "google.comz"
NO_ANSWER_HOST = "google"


class TestHostCheckDns:
    def test_dns_resolved(self):
        dns = src.hostcheck.dns.DNSCheck(VALID_HOST)
        result = dns.resolve()
        assert result and dns.status == src.hostcheck.dns.DNSStatus.OK

    def test_dns_not_exists(self):
        dns = src.hostcheck.dns.DNSCheck(NOT_EXISTS_HOST)
        result = dns.resolve()
        assert not result and dns.status == src.hostcheck.dns.DNSStatus.NOT_EXISTS

    def test_dns_no_answer(self):
        dns = src.hostcheck.dns.DNSCheck(NO_ANSWER_HOST)
        result = dns.resolve()
        assert not result and dns.status == src.hostcheck.dns.DNSStatus.NO_ANSWER

    def test_dns_to_text_is_str_on_resolved_host(self):
        dns = src.hostcheck.dns.DNSCheck(VALID_HOST)
        dns.resolve()
        assert isinstance(dns.to_text(), str)

    def test_dns_to_text_is_str_on_not_existing_host(self):
        dns = src.hostcheck.dns.DNSCheck(NOT_EXISTS_HOST)
        dns.resolve()
        assert isinstance(dns.to_text(), str)
