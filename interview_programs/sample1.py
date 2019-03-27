# import logging
# log = logging.getLogger(__name__)
# logging.basicConfig( level=logging.DEBUG,format='%(levelname)s:%(asctime)s::%(message)s')
#
#
# def sum(a, b):
#     log.info("Entering into sum method")
#     return a+b
# print(__name__)
#
# def sub(a,b):
#     log.info("Entering into sub method")
#     return a-b
#
#
# add = sum(150, 20)
# log.info("the value is {}".format(add))
# subt = sub(250, 10)
# log.info("the value is {}".format(subt))
#
#
#
# import re
# output = {'Audit-Session-ID': '010b850d000000b25ac57a08', 'IP Override': '0.0.0.0', 'Lifetime': '1506', 'Station': '6c:40:08:8c:7e:7a', 'Type': 'RSN', 'Username': 'cisco', 'VLAN Override': ''}
# output = str(output)
# m = re.search(r"\'Station\'\:\s*(\'[\w\:]+\')",output)
# print (m)
# print (m.group(1))
#
#
#
#
#
#
#
#
#
#
# """
# import sys
# sys.stderr.write("apathapa\n")
# sys.stderr.flush()
# sys.stdout.write("apathapa\n")
# print (sys.argv)
#
# sys.path.append("git_practice//")
# #from multi_threading.sample2 import sample2
# #from multi_threading.sample2 import *
# import multi_threading.sample2
#
#
# class A():
#     def __init__(self):
#
#         #sa.test(self)
#     def junk(self):
#         print("###")
# a = A()
# print w
# """
a = """
router bgp 65511
as-league
!
bgp update-delay 300 always
bgp graceful-restart
address-family ipv4 unicast
!
address-family vpnv4 unicast
!
neighbor 125.1.1.2
remote-as 65511
!
neighbor 125.1.2.2
remote-as 65500
!
!"""
b = """
router bgp 65511
as-league
!
bgp update-delay 300 always
bgp graceful-restart
address-family ipv4 unicast
!
address-family vpnv4 unicast
!
neighbor 125.1.1.2
remote-as 65511
timers 80 240 50
graceful-restart restart-time 140
graceful-restart stalepath-time 420
graceful-restart
!
neighbor 125.1.2.2
remote-as 65500
timers 80 240 50
graceful-restart restart-time 140
graceful-restart stalepath-time 420
graceful-restart
!
!"""

aa = a.split("!")
#print(aa)
ad = []
for i in aa:

    if  i !="\n" or i !="!" or len(i)>1:
        ele = i.split("\n")
        #print(ele)
        l = []
        for k in ele:
            if k :
             l.append(k)
        if l:
            ad.append(l)
print(ad)

bb = b.split("!")
#print(bb)
mad = []
jj = {}
for m in bb:
    if m != "\n" or m != "!" or len(m) > 1:
        ele = m.split("\n")
        #print(ele)
        ml = []
        for mk in ele:
            if mk:
                ml.append(mk)
        if ml:
            mad.append(ml)
print(mad)
if len(ad) == len(mad):
    o = []
    for dc,v in zip(ad,mad):
        if len(dc) > len(v):
            for ff in dc:
                if ff in v:
                    print("presented1")
                else:
                    print("not presented1")
        else:
            i = 0

            ki = []
            for ff in v:
                if ff in dc :
                    print("presented")
                    if i == 0:
                        first_element=ff
                        i = i+ 1
                else:
                    print("not presented")
                    ki.append(ff)
            if ki:
                jj.update({first_element:ki})
print(first_element)
print(jj)
for k,v in jj.items():
    print("The missed cli's under  {} are {}".format(k,v))
