# -*- coding: utf-8 -*-
__author__ = 'nmarchenko'

'''
    http://www.checkio.org/mission/task/info/bit-message/python-27/
'''

import datetime

import sys


def get_datetime(data):
    print data[2:16]
    d = data[2:16][::-1]
    for i, v in enumerate(d):
        if not i % 2:
            sys.stdout.write(str(i) + ":" +str(i+1))
            sys.stdout.write(' ')
        sys.stdout.write(v)
        if i % 2:
            sys.stdout.write('\n')
    sys.stdout.write('\n')

    print d[12:14]

    dd = datetime.datetime(
        2000 + int(d[12:14]),
        int(d[10:12]),
        int(d[8:10]),
        int(d[6:8]),
        int(d[4:6]),
        int(d[2:4]),
        tzinfo=datetime.datetime.tzinfo(None, -14400))

    # print data[2:16][::-1]
    # print "{0[2]}{0[3]}".format(data[2:16][::-1])
    # print data[2:8:][::-1]
    # print data[8:14:][::-1]
    # print data[14:16:][::-1]
    print dd


def checkio(data):
    print data[:2]
    print data[2:8]
    print data[8:14]
    print data[14:16]

    return []

import unittest


class _test(unittest.TestCase):

    def test_00(self):
        self.assertEqual(get_datetime(u'002080629173148007EDF27C1E3E9701'), '26 Aug 2002 19:37:41 GMT +2')

    def test_01(self):
        self.assertEqual(get_datetime(u'00317050201171820FD3323BDC0ED341C4303DEC3E8700'), '05 Jul 2013 02:11:17 GMT +7')

    def test_02(self):
        self.assertEqual(get_datetime(u'000130925161956915C8729E054A82C26D50DA0D7296EFA0EC5BBE06'), '29 Mar 2010 15:16:59 GMT -4')

    def test_03(self):
        self.assertEqual(get_datetime(u'08071010101010611F04180441043A043B044E04470435043D043804350020043F043E04340442043204350440043604340430043504420020043F0440043004320438043B043E'), '01 Jan 1970 01:01:01 GMT +4')

    def test_04(self):
        self.assertEqual(get_datetime(u'088310913041804C23805E4E0D82E5805E4E4B002C805E4E4B4E0D82E5898B4E4B002C898B4E4B4E0D82E577E54E4B002C77E54E4B4E0D82E5884C4E4B002C5B7881F365BC884C4E4B800C6B6277E3'), '19 Jan 2038 03:14:08 GMT -11')



    # def test_00(self):s
    #     self.assertEqual(checkio(u'002080629173148007EDF27C1E3E9701'), ['26 Aug 2002 19:37:41 GMT +2', 7, u'message'])

    # def test_01(self):
    #     self.assertTrue((checkio(u'00317050201171820FD3323BDC0ED341C4303DEC3E8700') ==
    #                      ['05 Jul 2013 02:11:17 GMT +7', 15, u'Selamat Datang!']))
    #
    # def test_02(self):
    #     self.assertTrue((checkio(u'000130925161956915C8729E054A82C26D50DA0D7296EFA0EC5BBE06') ==
    #                      ['29 Mar 2010 15:16:59 GMT -4', 21,
    #                       u'Hey, I am in New York']))
    #
    # def test_03(self):
    #     self.assertTrue((checkio(
    #         u'08071010101010611F04180441043A043B044E04470435043D043804350020043F043E04340442043204350440043604340430043504420020043F0440043004320438043B043E') ==
    #                      ['01 Jan 1970 01:01:01 GMT +4', 31,
    #                       u'Исключение подтверждает правило']))
    #
    # def test_04(self):
    #     self.assertTrue((checkio(
    #         u'088310913041804C23805E4E0D82E5805E4E4B002C805E4E4B4E0D82E5898B4E4B002C898B4E4B4E0D82E577E54E4B002C77E54E4B4E0D82E5884C4E4B002C5B7881F365BC884C4E4B800C6B6277E3 ') ==
    #                      ['19 Jan 2038 03:14:08 GMT -11', 35, u'聞不若聞之,聞之不若見之,見之不若知之,知之不若行之,學至於行之而止矣']))