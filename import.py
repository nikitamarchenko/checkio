__author__ = 'nmarchenko'

input ='''
[
        {
            "input": [1, 3],
            "answer":"0.(3)"
        },
        {
            "input": [5, 3],
            "answer":"1.(6)"
        },
        {
            "input": [3, 8],
            "answer":"0.375"
        },
        {
            "input": [7, 11],
            "answer":"0.(63)"
        },
        {
            "input": [29, 12],
            "answer":"2.41(6)"
        },
        {
            "input": [11, 7],
            "answer":"1.(571428)"
        },
        {
            "input": [23, 2],
            "answer":"11.5"
        },
        {
            "input": [2, 21],
            "answer":"0.(095238)"
        },
        {
            "input": [1, 17],
            "answer":"0.(0588235294117647)"
        },
        {
            "input": [58, 23],
            "answer":"2.(5217391304347826086956)"
        },
        {
            "input": [2, 3],
            "answer":"0.(6)"
        },
        {
            "input": [5, 2],
            "answer":"2.5"
        },
        {
            "input": [6, 4],
            "answer":"1.5"
        },
        {
            "input": [20, 6],
            "answer":"3.(3)"
        },
        {
            "input": [11, 13],
            "answer":"0.(846153)"
        },
        {
            "input": [22, 13],
            "answer":"1.(692307)"
        },
        {
            "input": [18, 23],
            "answer":"0.(7826086956521739130434)"
        },
        {
            "input": [30, 23],
            "answer":"1.(3043478260869565217391)"
        },
        {
            "input": [10, 12],
            "answer":"0.8(3)"
        },
        {
            "input": [41, 12],
            "answer":"3.41(6)"
        }
    ]

'''

import json

for i, v in enumerate(json.loads(input)):
    print """
    def test_{test:02d}(self):
        self.assertEqual(checkio({input}), '{answer}')""".format(test=i,**v)