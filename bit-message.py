# -*- coding: utf-8 -*-
__author__ = 'nmarchenko'

'''
    http://www.checkio.org/mission/task/info/bit-message/python-27/
'''


def checkio(data):

    def chunks(l, n):
        """ Yield successive n-sized chunks from l.
        """
        for i in xrange(0, len(l), n):
            yield l[i:i+n]

    def clearBit(int_type, offset):
        mask = ~(1 << offset)
        return (int_type & mask)

    def dprint(data):
        print '\n'.join('{0} {1:08b} {1}'.format(i, clearBit(int(c, 16), 7)) for i, c in enumerate(chunks(data, 2)))

    #dprint("FFFF00"[0:4])


    dprint(data[:16])

    #print '\n'.join('{0:08b}'.format(int(c, 16)) for c in chunks('E834', 2))

    # def clearBit(int_type, offset):
    #     mask = ~(1 << offset)
    #     return (int_type & mask)
    #
    # print '\n'.join('{0:08b}'.format(clearBit(int(c, 16), 7)) for c in chunks('FFFF', 2))

    #print '\n'.join('{0:08b}'.format(int(c, 16)) for c in chunks(data, 2))



    return []
#00 20 80 62 91 73 14 80 07 ED F2 7C 1E 3E 97 01
#   02 08 26 19 37 41
import unittest


class _test(unittest.TestCase):
    def test_00(self):
        self.assertTrue(checkio(u'002080629173148007EDF27C1E3E9701') ==
                        ['26 Aug 2002 19:37:41 GMT +2', 7, u'message'])

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