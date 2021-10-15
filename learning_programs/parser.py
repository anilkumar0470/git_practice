# import sys
# import optparse
#
# parser = optparse.OptionParser()
# parser.add_option('-n', '--name', dest='name', help='Your Name')
# parser.add_option('-a', '--age', dest='age', help='Your Age', type=int)
#
# (args, options) = parser.parse_args()
# print (options)
# print (args)

#
# import requests
#
# rrr = requests.post('https://httpbin.org/post', data={'name': 'junk'})
# print(rrr.status_code)
# out = requests.get('https://httpbin.org/get')
# import pdb
# pdb.set_trace()

# import time
# def a() :
#     start_time = time.time()
#     time.sleep(5)
#     print("time difference is {}".format(time.time() - start_time))
#
# a()
# a()


class SingleTone:
    def __new__(cls):
        print("I am in __new__ magic method")
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingleTone, cls).__new__(cls)
        return cls.instance



    def __init__(cls):
        print("I am in __init__ magic method")
        # if not hasattr(cls, 'instance'):
        #     cls.instance = super(SingleTone, cls).__new__(cls)
        # return cls.instance
    def samp(self):
        print("sampe")


# class SingleTone:
#
#     pass


s1 = SingleTone()
s1.samp()
s2 = SingleTone()
























