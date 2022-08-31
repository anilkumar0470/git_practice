# # # Python program to find the factorial of a number provided by the user.
# #
# # # take input from the user
# # # num = int(input("Enter a number: "))
# # num = 10
# # factorial = 1
# #
# # # check if the number is negative, positive or zero
# # if num < 0:
# #     print("Sorry, factorial does not exist for negative numbers")
# # elif num == 0:
# #     print("The factorial of 0 is 1")
# # else:
# #     for i in range(1,num + 1):
# #         factorial = factorial*i
# #     print("The factorial of",num,"is",factorial)
# #
# #
# # for i in range(10):
# #     print(i)
# # else:
# #     print("apathapa")
# #
# #
# # list1 = [1,2,3,4,5,6]
# # list2 = list1
# # list2.append(7)
# # print(list1)
# # print(list2)
# #
# #
# # import re
# # str = "apathapa 123 hello"
# # match = re.search("\w+\s*\d+", str)
# # print(match.group())
# # print(match.groups())
# #
# #
# #
# # list12  = ['a', 'r', 'd', '3', 'u', '8', 'e', '2', 'w', '2', 't']
# #
# # list12.sort()
# # print(list12)
# #
# #
#
# str1 = """show remote-lan all\nRemote-LAN Profile Name     : prof-RANCISCO/BLD_SF/FLOOR2-P2\n================================================\nIdentifier                                     : 1\nStatus                                         : Enabled\nMac-filtering                                  : dnac-cts-GUESTtb1-cc01b498\nNumber of Active Clients                       : 0\nSecurity_8021x_dot1x                           : Enabled\n8021.x Authentication list name                : dnac-cts-GUESTtb1-cc01b498\nLocal Auth eap Profile Name                    : Not Configured\nWeb Auth Security                              : Disabled\nWebauth Authentication list name               : Not Configured\nWeb Auth Parameter Map                         : Not Configured\nClient association limit                       : 0\nIpv4 Web Pre Auth Acl                          : Not Configured\nIpv6 Web Pre Auth Acl                          : Not Configured\nmDNS Gateway Status                            : Bridge\nAuthentication Fallback Status                 : Dot1X to MAC-filtering\n\nRemote-LAN Profile Name     : prof-RANCISCO/BLD_SF/FLOOR2-P1\n================================================\nIdentifier                                     : 2\nStatus                                         : Enabled\nMac-filtering                                  : dnac-cts-GUESTtb1-cc01b498\nNumber of Active Clients                       : 1\nSecurity_8021x_dot1x                           : Enabled\n8021.x Authentication list name                : dnac-cts-GUESTtb1-cc01b498\nLocal Auth eap Profile Name                    : Not Configured\nWeb Auth Security                              : Disabled\nWebauth Authentication list name               : Not Configured\nWeb Auth Parameter Map                         : Not Configured\nClient association limit                       : 0\nIpv4 Web Pre Auth Acl                          : Not Configured\nIpv6 Web Pre Auth Acl                          : Not Configured\nmDNS Gateway Status                            : Bridge\nAuthentication Fallback Status                 : MAC-filtering to Dot1X\n\nRemote-LAN Profile Name     : prof-RANCISCO/BLD_SF/FLOOR2-P3\n================================================\nIdentifier                                     : 3\nStatus                                         : Enabled\nMac-filtering                                  : Not Configured\nNumber of Active Clients                       : 0\nSecurity_8021x_dot1x                           : Enabled\n8021.x Authentication list name                : dnac-cts-GUESTtb1-cc01b498\nLocal Auth eap Profile Name                    : Not Configured\nWeb Auth Security                              : Disabled\nWebauth Authentication list name               : Not Configured\nWeb Auth Parameter Map                         : Not Configured\nClient association limit                       : 0\nIpv4 Web Pre Auth Acl                          : Not Configured\nIpv6 Web Pre Auth Acl                          : Not Configured\nmDNS Gateway Status                            : Bridge\nAuthentication Fallback Status                 : Not Configured\n\nTB1-VEWLC#
# """
list1 = [{
'portId': 1,
'portStatus': True,
'l2AuthType': 'DOT1X',
'l3AuthType': 'OPEN',
'isMACfilteringEnabled': False,
'authTimeout': 1800,
'maximumEndpoints': 0,
'poeStatus': False,
'poePowerLevel': 1,
'profileName': 'prof-RANCISCO/BLD_SF/FLOOR2-P1',
'rlanDescription': '',
'policyName': 'pol-RANCISCO/BLD_SF/FLOOR2-P1',
'authListName': '',
'fallbackType': '1',
'isFabric': True,
'fabricProfileName': 'pol-RANCISCO/BLD_SF/FLOOR2-P1',
'ipAddressPool': '',
'scalableGroupTag': '',
'managedSites': [''],
'networkDeviceId': ''
}, {
'portId': 2,
'portStatus': True,
'l2AuthType': 'DOT1X',
'l3AuthType': 'OPEN',
'isMACfilteringEnabled': True,
'authTimeout': 1800,
'maximumEndpoints': 0,
'poeStatus': False,
'poePowerLevel': 1,
'profileName': 'prof-RANCISCO/BLD_SF/FLOOR2-P2',
'rlanDescription': '',
'policyName': 'pol-RANCISCO/BLD_SF/FLOOR2-P2',
'authListName': '',
'fallbackType': '2',
'isFabric': True,
'fabricProfileName': 'pol-RANCISCO/BLD_SF/FLOOR2-P2',
'ipAddressPool': '',
'scalableGroupTag': '',
'managedSites': [''],
'networkDeviceId': ''
}, {
'portId': 3,
'portStatus': True,
'l2AuthType': 'DOT1X',
'l3AuthType': 'OPEN',
'isMACfilteringEnabled': True,
'authTimeout': 1800,
'maximumEndpoints': 0,
'poeStatus': False,
'poePowerLevel': 1,
'profileName': 'prof-RANCISCO/BLD_SF/FLOOR2-P3',
'rlanDescription': '',
'policyName': 'pol-RANCISCO/BLD_SF/FLOOR2-P3',
'authListName': '',
'fallbackType': '0',
'isFabric': True,
'fabricProfileName': 'pol-RANCISCO/BLD_SF/FLOOR2-P3',
'ipAddressPool': '',
'scalableGroupTag': '',
'managedSites': [''],
'networkDeviceId': ''
}]
#
# import re
# for item in list1:
#     flag = False
#     for line in str1.split("\n"):
#         pattern1 = "Identifier\s+\:\s+{}".format(item["portId"])
#         if re.search(pattern1, line):
#             # print("item id {}".format(item["portId"]))
#             flag = True
#         else:
#             if flag:
#                 if item["fallbackType"] == 0:
#                     if "Authentication Fallback Status" in line:
#                         pattern2 = "Authentication\s+Fallback\s+Status\s+\:\s+(Dot1X\s+to\s+MAC\-filtering)"
#                         match2 = re.search(pattern2, line)
#                         if match2:
#                             print("Authentication Fallback Status is as expected {} for portid {}".format(match2.group(1), item["portId"]))
#                             flag = False
#                         else:
#                             print("Authentication Fallback Status is not matching got {}".format(line))
#                             flag = False
#                     pass
#                 elif item["fallbackType"] == "1":
#                     if "Authentication Fallback Status" in line:
#                         pattern4 = "Authentication\s+Fallback\s+Status\s+\:\s+(Not\s+Configured)"
#                         match4 = re.search(pattern4, line)
#                         if match4:
#                             print("Authentication Fallback Status is as expected for portid {}".format(match4.group(1), item["portId"]))
#                             flag = False
#                         else:
#                             print("Authentication Fallback Status is not matching got {}".format(line))
#                             flag = False
#                         pass
#
#                 elif item["fallbackType"] == "2":
#                     # print("222")
#                     if "Authentication Fallback Status" in line:
#                         pattern3 = "Authentication\s+Fallback\s+Status\s+\:\s+(MAC\-filtering\s+to\s+Dot1X)"
#                         match3 = re.search(pattern3, line)
#                         if match3:
#                             print("Authentication Fallback Status is as expected for portid {}".format(match3.group(1), item["portId"]))
#                             flag = False
#                         else:
#                             print("Authentication Fallback Status is not matching got {}".format(line))
#                             flag = False
#                         pass
#



str1="""show remote-lan all\nRemote-LAN Profile Name     : prof-RANCISCO/BLD_SF/FLOOR2-P52\n================================================\nIdentifier                                     : 1\nStatus                                         : Enablwed\nMac-filtering                                  : dnac-cts-GUESTtb1-cc01b498\nNumber of Active Clients                       : 0\nSecurity_8021x_dot1x                           : Enabled\n8021.x Authentication list name                : dnac-cts-GUESTtb1-cc01b498\nLocal Auth eap Profile Name                    : Not Configured\nWeb Auth Security                              : Disabled\nWebauth Authentication list name               : Not Configured\nWeb Auth Parameter Map                         : Not Configured\nClient association limit                       : 0\nIpv4 Web Pre Auth Acl                          : Not Configured\nIpv6 Web Pre Auth Acl                          : Not Configured\nmDNS Gateway Status                            : Bridge\nAuthentication Fallback Status                 : Dot1X to MAC-filtering\n\nRemote-LAN Profile Name     : prof-RANCISCO/BLD_SF/FLOOR2-P1\n================================================\nIdentifier                                     : 2\nStatus                                         : Enabled\nMac-filtering                                  : dnac-cts-GUESTtb1-cc01b498\nNumber of Active Clients                       : 1\nSecurity_8021x_dot1x                           : Enabled\n8021.x Authentication list name                : dnac-cts-GUESTtb1-cc01b498\nLocal Auth eap Profile Name                    : Not Configured\nWeb Auth Security                              : Disabled\nWebauth Authentication list name               : Not Configured\nWeb Auth Parameter Map                         : Not Configured\nClient association limit                       : 0\nIpv4 Web Pre Auth Acl                          : Not Configured\nIpv6 Web Pre Auth Acl                          : Not Configured\nmDNS Gateway Status                            : Bridge\nAuthentication Fallback Status                 : MAC-filtering to Dot1X\n\nRemote-LAN Profile Name     : prof-RANCISCO/BLD_SF/FLOOR2-P3\n================================================\nIdentifier                                     : 3\nStatus                                         : Enabled\nMac-filtering                                  : Not Configured\nNumber of Active Clients                       : 0\nSecurity_8021x_dot1x                           : Enabled\n8021.x Authentication list name                : dnac-cts-GUESTtb1-cc01b498\nLocal Auth eap Profile Name                    : Not Configured\nWeb Auth Security                              : Disabled\nWebauth Authentication list name               : Not Configured\nWeb Auth Parameter Map                         : Not Configured\nClient association limit                       : 0\nIpv4 Web Pre Auth Acl                          : Not Configured\nIpv6 Web Pre Auth Acl                          : Not Configured\nmDNS Gateway Status                            : Bridge\nAuthentication Fallback Status                 : Not Configured\n\nTB1-VEWLC#
"""
import re
for item in list1:
    profile_flag = False
    status_flag = False
    new_flag = False
    for line in str1.split("\n"):
        pattern1 = "Remote-LAN\s+Profile\s+Name\s+\:\s+{}".format(item["profileName"])
        if re.search(pattern1, line):
            # print("matched {}".format(item["profileName"]))
            profile_flag = True
            count = 0
        if profile_flag:
            count += 1
            if count == 5:
                new_flag = True

                continue
            if not new_flag:
                if re.search("Status\s+:\s+Enabled", line):
                    status_flag = True
        if status_flag:
                if item["fallbackType"] == "2":
                    if "Authentication Fallback Status" in line:
                        pattern2 = "Authentication\s+Fallback\s+Status\s+\:\s+(Dot1X\s+to\s+MAC\-filtering)"
                        match2 = re.search(pattern2, line)
                        if match2:
                            print("Authentication Fallback Status is as expected :{} for {}".format(match2.group(1), item["profileName"]))
                            profile_flag = False
                            break
                        else:
                            print("22")
                            print("Authentication Fallback Status is not matching for {} got {}".format( item["profileName"],line))
                            profile_flag = False
                            break

                elif item["fallbackType"] == '0':
                    if "Authentication Fallback Status" in line:
                        pattern4 = "Authentication\s+Fallback\s+Status\s+\:\s+(Not\s+Configured)"
                        match4 = re.search(pattern4, line)
                        if match4:
                            print("Authentication Fallback Status is as expected :{} for {}".format(match4.group(1), item["profileName"]))
                            profile_flag = False
                            break
                        else:
                            print("23")
                            print("Authentication Fallback Status is not matching got {}".format(line))
                            profile_flag = False
                            break

                elif item["fallbackType"] == "1":
                    if "Authentication Fallback Status" in line:
                        pattern3 = "Authentication\s+Fallback\s+Status\s+\:\s+(MAC\-filtering\s+to\s+Dot1X)"
                        match3 = re.search(pattern3, line)
                        if match3:
                            print("Authentication Fallback Status is as expected :{} for {}".format(match3.group(1), item["profileName"]))
                            profile_flag = False
                            break
                        else:
                            print("24")
                            print("Authentication Fallback Status is not matching got {}".format(line))
                            profile_flag = False
                            break

    else:
        if not status_flag and profile_flag:
            print("status  is not matching for {}".format(item["profileName"]))
        if not profile_flag:
            print("profile name is not matching for {}".format(item["profileName"]))

