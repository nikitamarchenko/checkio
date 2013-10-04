__author__ = 'nmarchenko'

#print 0.0 in {0.1 + 0.1 + 0.1 - 0.3: True}


#print {'name': 'Dima', 'role': 'dev'} == {'name': 'Dima', 'role': 'dev'}

# data = [
#     {'name': 'Dima', 'role': 'dev'},
#     {'name': 'Tatyana', 'role': 'QA'},
#     {'name': 'Dima', 'role': 'dev'}
# ]
#
# print [dict(y) for y in set(tuple(x.items()) for x in data)]
#
#

import os

try:
    data = os.environ['VCAP_SERVICES']
except KeyError:
    print "VCAP_SERVICES not found in env"
    exit(-1)

import json
from pprint import pprint

postgre = json.loads(data)['postgresql-9.2'][0]

pprint(postgre) #for debug

print postgre['credentials']['username'] # username

import psycopg2

with psycopg2.connect(postgre['credentials']['uri']) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM test;")
        print cur.fetchone()

result = cur.fetchone()
print result[0]
print result[1]
print result[2]
