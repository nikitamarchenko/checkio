__author__ = 'tpuctah'


def checkio(data):
    print map(lambda x: 0 <= int(x) < 256, '192.168.1.1'.split('.'))
    print [ip for ip in data.split(' ') if ip.count('.') == 3]
    return [ip for ip in data.split(' ') if ip.count('.') == 3 and all(map(lambda x: 0 <= int(x) < 256, ip.split('.')))]


assert checkio("192.168.1.1 and 10.0.0.1 or 127.0.0.1") == ["192.168.1.1", "10.0.0.1", "127.0.0.1"]
assert checkio(u"10.0.0.1.1 but 127.0.0.256 1.1.1.1") == ["1.1.1.1"]
assert checkio("167.11.0.0 1.2.3.255 192,168,1,1") == ["167.11.0.0", "1.2.3.255"]
assert checkio("267.11.0.0 1.2.3.4/16 192:168:1:1") == ["1.2.3.4"]