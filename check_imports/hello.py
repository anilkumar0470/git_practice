
#
# #
# # courses = ['telugu', 'english', 'maths']
# # # sample()
# # # print(test)
# #
# # import sys
# # sys.path.append("/home/test/Desktop")
# # print(sys.path)
# #
# # from hai import junk, test
# # # def sample1():
# # #     print("sample1")
# # #
# # # def sample2():
# # #
# # #     print("sample2")
# # #
# # # def sample3():
# # #     print("sample3")
# #
# # fd = open()
#
#
#
# import requests
# import json
# import hashlib
# import base64
# import time
# import hmac
# import pandas as pd
# #Account Info
# AccessId = 'n97rqkp7nnry76MK4yk6'
# AccessKey ='9[HU5C8K=69V{y%]v6)bKS8EfUZVxp)r^6+5m+h+'
# Company = 'connxai'
#
# #Request Info
# httpVerb ='GET'
# resourcePath = '/device/devices'
# queryParams =''
# data = ''
#
# #Construct URL
# url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath +queryParams
#
# #Get current time in milliseconds
# epoch = str(int(time.time() * 1000))
#
# #Concatenate Request details
# requestVars = httpVerb + epoch + data + resourcePath
#
#
# #Construct signature
# hmac1 = hmac.new(AccessKey.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest()
# signature = base64.b64encode(hmac1.encode())
#
# #Construct headers
# auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
# headers = {'Content-Type':'application/json','Authorization':auth}
#
# #Make request
# response = requests.get(url, data=data, headers=headers)
#
# #Print status and body of response
# # print('Response Status:',response.status_code)
#
# json_content = response.json()
# device_ids = []
# for element in json_content['data']['items']:
#     device_ids.append(element['id'])
# # import pdb
# # pdb.set_trace()
# # json_content['data']['items'][0]['id']
# with open("hello.txt", 'w') as fd:
#     final_dict = {}
#     for device_id in device_ids:
#         #Account Info
#         AccessId = 'n97rqkp7nnry76MK4yk6'
#         AccessKey ='9[HU5C8K=69V{y%]v6)bKS8EfUZVxp)r^6+5m+h+'
#         Company = 'connxai'
#
#         #Request Info
#         httpVerb ='GET'
#         resourcePath = '/device/devices/{}/devicedatasources'.format(device_id)
#         queryParams =''
#         data = ''
#
#         #Construct URL
#         url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath +queryParams
#
#         #Get current time in milliseconds
#         epoch = str(int(time.time() * 1000))
#
#         #Concatenate Request details
#         requestVars = httpVerb + epoch + data + resourcePath
#
#
#         #Construct signature
#         hmac1 = hmac.new(AccessKey.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest()
#         signature = base64.b64encode(hmac1.encode())
#
#         #Construct headers
#         auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
#         headers = {'Content-Type':'application/json','Authorization':auth}
#
#         #Make request
#         response = requests.get(url, data=data, headers=headers)
#
#         #Print status and body of response
#         # print('Response Status:',response.status_code)
#
#         json_content = response.json()
#         # print(json_content)
#         list_of_ids = []
#         value = json_content['data']['items']
#         for element in json_content['data']['items']:
#             list_of_ids.append(element['id'])
#         print(device_id, list_of_ids)
#         new_dict = {}
#         for list_of_id in list_of_ids:
#             #Account Info
#             AccessId = 'n97rqkp7nnry76MK4yk6'
#             AccessKey ='9[HU5C8K=69V{y%]v6)bKS8EfUZVxp)r^6+5m+h+'
#             Company = 'connxai'
#
#             #Request Info
#             httpVerb ='GET'
#             resourcePath = '/device/devices/{}/devicedatasources/{}/data'.format(device_id, list_of_id)
#             queryParams =''
#             data = ''
#
#             #Construct URL
#             url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath +queryParams
#
#             #Get current time in milliseconds
#             epoch = str(int(time.time() * 1000))
#
#             #Concatenate Request details
#             requestVars = httpVerb + epoch + data + resourcePath
#
#
#             #Construct signature
#             hmac1 = hmac.new(AccessKey.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest()
#             signature = base64.b64encode(hmac1.encode())
#
#             #Construct headers
#             auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
#             headers = {'Content-Type':'application/json','Authorization':auth}
#
#             #Make request
#
#             dict  = {}
#             response = requests.get(url, data=data, headers=headers)
#             sam_out = response.json()
#             dict.update({'instance': sam_out['data']['instances']})
#             dict.update({'dataSourceName': sam_out['data']['dataSourceName']})
#             dict.update({'dataPoints': sam_out['data']['dataPoints']})
#             new_dict.update({list_of_id:dict})
#             sample = {list_of_id:dict}
#             final_dict.update({device_id: sample})
#             print(final_dict)
#             fd.write("="*60)
#             fd.write(str(final_dict))
#
#
#
# print(final_dict)
# #
# # resourcePath1  = '/device/devices/405/devicedatasources/20994/data/'
# # new_url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath1 +queryParams
# #
# # response1 = requests.get(url=new_url, data=data, headers=headers)
# # print(response1.json())
#
# # print(response.text)
# # q = response.json()
# # print(q)
# # m =(q['data'])
# # final = pd.json_normalize(m)
# # print(final)
# # # final.to_csv("5.csv")

d = {"name": "anu",
"loc": "bang"}

import json
print(type(d))
out = json.dumps(d)
print(out)
print(type(out))