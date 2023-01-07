#!/usr/bin/env python

"""Tests for `python_malicious_url_block` package."""


import unittest

from python_malicious_url_block import url_block


class TestPython_malicious_url_block(unittest.TestCase):
    """Tests for `python_malicious_url_block` package."""

    def test_check_url_unsafe(self):
        test = url_block()

        result = test.check_safe("0ed7.rate.coinangel.online")
        self.assertEqual(result, False)

        result = test.check_safe("residenciaestudiantesjardines.com")
        self.assertEqual(result, False)


        result = test.check_safe("vitanigoldtravelandtours.com")
        self.assertEqual(result, False)

        result = test.check_safe("117.221.186.170")
        self.assertEqual(result, False)


    def test_check_url_safe(self):
        test = url_block()

        result = test.check_safe("google.com")
        self.assertEqual(result, True)


        result = test.check_safe("www.khara.co.jp")
        self.assertEqual(result, True)

        
        result = test.check_safe("yahoo.co.jp")
        self.assertEqual(result, True)


    def test_check_url_append_url(self):
        filter_list = [
            "https://malware-filter.gitlab.io/malware-filter/pup-filter-domains.txt",

        ]
        test = url_block(filter_url=filter_list)

        result = test.check_safe("google.com")
        self.assertEqual(result, True)


        result = test.check_safe("www.khara.co.jp")
        self.assertEqual(result, True)

        
        result = test.check_safe("yahoo.co.jp")
        self.assertEqual(result, True)

        result = test.check_safe("hansview.ru")
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()


